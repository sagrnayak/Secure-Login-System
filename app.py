# -------------------- IMPORTS --------------------
from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
import sqlite3
import random   # Used for OTP generation

# -------------------- APP SETUP --------------------
app = Flask(__name__)
app.secret_key = "supersecretkey"  # Used to secure sessions

bcrypt = Bcrypt(app)


# -------------------- DATABASE SETUP --------------------
def init_db():
    """
    Creates users table if it doesn't exist.
    """
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


# -------------------- HOME --------------------
@app.route("/")
def home():
    """
    Redirect user based on login status.
    """
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


# -------------------- REGISTER --------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handles user registration with password hashing.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Basic input validation
        if len(username) < 3 or len(password) < 5:
            return "Invalid input (min username=3, password=5)"

        # Hash password securely using bcrypt
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()

            # Parameterized query prevents SQL injection
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                        (username, hashed_pw))

            conn.commit()
            conn.close()

            return redirect("/login")

        except:
            return "User already exists"

    return render_template("register.html")


# -------------------- LOGIN (STEP 1: PASSWORD CHECK) --------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Step 1: Verify username & password.
    If correct → generate OTP and move to 2FA step.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cur = conn.cursor()

        # Safe query (prevents SQL injection)
        cur.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cur.fetchone()

        conn.close()

        if user:
            stored_hash = user[0]

            # Check password with bcrypt
            if bcrypt.check_password_hash(stored_hash, password):

                # -------------------- GENERATE OTP --------------------
                otp = str(random.randint(100000, 999999))

                # Store OTP and temp user in session
                session["otp"] = otp
                session["temp_user"] = username

                # For demo → print OTP in terminal
                print(f"[DEBUG OTP]: {otp}")

                return redirect("/verify-otp")

        return "Invalid credentials"

    return render_template("login.html")


# -------------------- 2FA OTP VERIFICATION --------------------
@app.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    """
    Step 2: Verify OTP before final login.
    """
    if request.method == "POST":
        user_otp = request.form["otp"]

        # Check OTP match
        if "otp" in session and user_otp == session["otp"]:
            
            # Login successful → create session
            session["user"] = session["temp_user"]

            # Remove temporary data
            session.pop("otp", None)
            session.pop("temp_user", None)

            return redirect("/dashboard")

        return "Invalid OTP"

    return render_template("otp.html")


# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
def dashboard():
    """
    Protected route (only logged-in users allowed).
    """
    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html", user=session["user"])


# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    """
    Clears session and logs out user.
    """
    session.pop("user", None)
    return redirect("/login")


# -------------------- RUN APP --------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)