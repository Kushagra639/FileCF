# 🔐 FILE CF - Secure File Locker

A lightweight Python-based file encryption tool that allows users to securely encrypt and decrypt files using a password.

This project was built as part of my cybersecurity learning journey and demonstrates concepts such as password-based encryption, key derivation, cryptographic salts, authenticated encryption, and secure file handling.

---

## 🚀 Features

### 🔑 Password-Based Encryption

Encrypt files using a user-provided password.

The encryption key is derived securely from the password using PBKDF2.

---

### 🧂 Random Salt Generation

A unique cryptographic salt is generated for every encrypted file.

This protects against rainbow-table attacks and ensures that identical passwords generate different encryption keys.

---

### 🔒 Secure Key Derivation

Uses:

- PBKDF2-HMAC-SHA256
- 480,000 iterations
- 256-bit encryption keys

to derive strong encryption keys from user passwords.

---

### 🛡️ Fernet Authenticated Encryption

Uses the Fernet implementation from the Cryptography library.

Provides:

- Confidentiality
- Integrity Verification
- Authentication

This prevents unauthorized modification of encrypted files.

---

### 📁 Multi-File Support

Supports virtually any file type including:

- Text Files (.txt)
- PDFs (.pdf)
- Images (.png, .jpg, .jpeg)
- Videos
- ZIP Archives
- Binary Files
- Custom Extensions

---

### 🖥️ Graphical User Interface

Built using CustomTkinter for a modern desktop experience.

Features:

- File selection
- Password input
- Encryption & Decryption
- Theme switching
- User-friendly dialogs

---

### 🌗 Theme Support

Supports:

- Light Mode
- Dark Mode
- Custom Pastel Theme

---

## 📸 Screenshots

### Main Menu

![Main Menu Dark](/screenshots/Screenshot-1.png)
![Main Menu Light](/screenshots/Screenshot-2.png)

### Encryption Screen

![Encrypt Screen](/screenshots/Screenshot-3.png)

### Decryption Screen

![Decrypt Screen](/screenshots/Screenshot-4.png)

---

## 🛠️ Technologies Used

- Python 3
- Cryptography
- CustomTkinter
- Tkinter

---

## 📦 Installation & Setup

### Install Dependencies

```bash
pip install cryptography customtkinter
```

---

### Download the Source Code

*GUI version* (**Recommended**):

- [`main_gui.py`](/main_gui.py)
- [`encrypt_decrypt.py`](/encrypt_decrypt.py)
- [`pastel_theme.json`](/pastel_theme.json)

Alternatively, the *console version* can be used:

- [`main.py`](/main.py)
- [`encrypt_decrypt.py`](/encrypt_decrypt.py)

**Store all files in the same project folder.**

---

### Configure Theme File

In `main_gui.py`, locate:

```python
ctk.set_default_color_theme("pastel_theme.json")
```

Replace:

```python
"pastel_theme.json"
```

with the full path to your theme file, if necessary.

Example:

```python
ctk.set_default_color_theme(
    "C:\\Users\\YourName\\Desktop\\FileCF\\pastel_theme.json"
)
```

---

## ▶️ Usage

Run:

```bash
python main_gui.py
```

or

```bash
python main.py
```

Choose whether to encrypt or decrypt a file, select a file, and enter a password.

---

## 📋 Example Workflow

### Encryption

```text
Select File
       ↓
Enter Password
       ↓
Generate Salt
       ↓
Derive Encryption Key
       ↓
Encrypt File
       ↓
Save as:
example.pdf.encrypted
```

---

### Decryption

```text
Select Encrypted File
          ↓
Enter Password
          ↓
Extract Salt
          ↓
Derive Key
          ↓
Decrypt File
          ↓
Restore Original File
```

---

## ⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.

While the project uses industry-standard cryptographic libraries, it has not undergone independent security auditing and should not be relied upon for protecting highly sensitive or mission-critical data.

Users are responsible for evaluating its suitability for their specific use case.

---

## 🎯 Learning Objectives

This project helped me practice:

- Python Programming
- Cryptography Fundamentals
- Password-Based Encryption
- PBKDF2 Key Derivation
- Secure File Handling
- GUI Development
- Exception Handling
- Cybersecurity Fundamentals

---

## 🙋‍♂️ Author - 

Kushagra Aggarwal

- Cyber Security Enthusiast
- Computer Science Student
- Alumnus, Dr. B.R. Ambedkar SoSE, Karol Bagh

<p style="margin: 0; padding: 0;">
  <span style="font-weight: bold; font-size: 1.1em;">Follow me on: </span>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/LinkedIn%20Logo.png"
         alt="LinkedIn"
         width="20"
         style="display: block;">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/Instagram_logo.png"
         alt="Instagram"
         width="20"
         style="display: block;">
  </a>
</p>

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

Feel free to ⭐ the repository if you find it useful!
