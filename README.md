# 🔐 Secure Login System with 2FA

A secure web-based authentication system built using Flask that implements modern security practices such as password hashing, session management, and Two-Factor Authentication (2FA).

---

## 🚀 Features

* 🔑 User Registration & Login
* 🔒 Password Hashing using bcrypt
* 🛡️ Protection against SQL Injection (Parameterized Queries)
* 📦 SQLite Database Integration
* 🔐 Session Management (Login / Logout)
* 📲 Two-Factor Authentication (OTP-based)
* ⚡ Lightweight and beginner-friendly

---

## 🧠 How It Works

1. User registers with username and password
2. Password is securely hashed using bcrypt
3. During login:

   * Password is verified
   * A 6-digit OTP is generated
   * OTP is required to complete login (2FA)
4. Session is created after successful authentication
5. User can access protected dashboard

---

## 🛠️ Tech Stack

* Python
* Flask
* Flask-Bcrypt
* SQLite
* HTML (Jinja Templates)

---

## 📁 Project Structure

```
Secure-Login-System/
│── app.py
│── users.db
│── templates/
│    ├── login.html
│    ├── register.html
│    ├── dashboard.html
│    ├── otp.html
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/Secure-Login-System.git
cd Secure-Login-System
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 🔐 Security Features Explained

* **Password Hashing:**
  Passwords are never stored in plain text. They are hashed using bcrypt.

* **SQL Injection Protection:**
  Parameterized queries prevent malicious SQL inputs.

* **Session Management:**
  Flask sessions ensure only authenticated users access protected routes.

* **Two-Factor Authentication (2FA):**
  Adds an extra layer of security using OTP verification.

---

## ⚠️ Disclaimer

* This project is for educational purposes.
* OTP is displayed in the terminal (for demo only).
* In real-world applications, OTP should be sent via:

  * Email (SMTP)
  * SMS APIs
  * Authenticator apps (TOTP)

---

## 🔮 Future Improvements

* 📧 Email-based OTP
* 📱 Google Authenticator (TOTP)
* 🎨 Improved UI with Bootstrap
* 🌐 Deployment on cloud (Render / AWS)
* 🔐 JWT Authentication

---

## 💡 Author

Developed as a cybersecurity-focused mini project to demonstrate secure authentication practices.

---
