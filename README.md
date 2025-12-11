
# QR Code Generator with Secure User Authentication

A full-stack web application that combines **secure user authentication** with **dynamic QR code generation**.  
The project uses a **FastAPI** backend for API endpoints, **bcrypt** for password hashing, and a clean **HTML/CSS/JavaScript** frontend.

---

## ⭐ Features

### 🔐 Secure User Authentication
- Users can **register** and **log in**.
- Passwords are **hashed using bcrypt** before being stored.
- The database **never stores plain-text passwords**.
- Secure password verification during login (bcrypt hash comparison).

### 🧾 QR Code Generation
- Authenticated users can generate QR codes from any text or URL.
- Backend generates the QR code using Python libraries.
- The QR code is returned as an image and displayed on the frontend.
- Simple UI for input and preview.

### 💻 Clean Frontend
- `index.html` (homepage), `login.html`, and `qr.html` for QR generation.
- Styled using **CSS** and enhanced with **vanilla JavaScript**.
- Fully decoupled from backend for easy modification.

### ⚙️ FastAPI Backend
- RESTful API built with **FastAPI**.
- Endpoints for:
  - User registration  
  - User login  
  - QR code generation  
- Auto-generated documentation at `/docs`.

### 🗄️ Database Layer
- Lightweight Python database module to store user credentials.
- Passwords stored as **bcrypt hashes**.
- Easy to extend for SQLite, PostgreSQL, or MongoDB.

---

## 📁 Project Structure

```

.
├── index.html
├── login.html
├── qr.html
├── style.css
├── app.js
├── login.js
├── main.py
├── database.py
└── README.md

````

- **main.py** — FastAPI application (routes, hashing, QR generation)
- **database.py** — simple user data storage with bcrypt hashing
- ***.html / *.css / *.js** — frontend UI pages and scripts

---

## 🔧 Technologies Used

| Area        | Technology |
|-------------|------------|
| Backend     | FastAPI, Uvicorn |
| Security    | bcrypt (password hashing) |
| Frontend    | HTML, CSS, JavaScript |
| QR Creation | Python QR code libraries (e.g., `qrcode`) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/giboiq200/qr-code-generator.git
cd qr-code-generator
````

### 2. (Optional but recommended) Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn bcrypt qrcode[pil] python-multipart
```

---

## ▶️ Running the Application

### Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Your backend will be available at:

* **[http://localhost:8000](http://localhost:8000)**

### Open the Frontend

Simply open:

* `index.html` — homepage
* `login.html` — user login
* `qr.html` — QR generator (requires login via frontend JS)

---

## 📌 How Authentication Works

1. User registers through the frontend.
2. Backend receives credentials and:

   * Generates a bcrypt salt.
   * Hashes the password using bcrypt.
   * Stores the bcrypt hash in the database.
3. During login:

   * User enters email + password.
   * Backend fetches bcrypt hash from database.
   * bcrypt verifies whether the provided password matches the stored hash.
4. If valid, backend returns success and frontend redirects the user to QR generator page.

Passwords **never** appear in logs or the database.

---

## 🧩 How QR Code Generation Works

1. User enters text or a URL into the input field.
2. JavaScript sends the text to the FastAPI endpoint.
3. Backend generates a QR code image using a Python QR library.
4. Image is returned to frontend and displayed immediately.
5. User can save or screenshot the QR code.

---

## 🛠️ Customization

You can easily extend the project:

* Add JWT tokens for persistent login.
* Add a real database (SQLite/PostgreSQL/MongoDB).
* Log QR code generation history.
* Add user profiles.
* Implement QR code styling options (colors, logos, etc.).
* Deploy to Render, Railway, or Docker.

---

## 🤝 Contributing

Contributions are welcome!
To contribute:

1. Fork the repository.
2. Create a new branch (`feature/my-update`).
3. Commit and push your changes.
4. Open a Pull Request.

---

## 📄 License

This project is free to use for everyone**.

---

## 🙋 Support & Questions

If you have questions, issues, or feature suggestions:

* Open an issue in the repository.
* Contact the project owner through GitHub.

---

Thank you for checking out **QR Code Generator with Authentication**!
Enjoy building and generating QR codes securely! 🚀
