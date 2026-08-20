# 🔐 Caesar Cipher

A simple Python command-line tool to **encrypt** and **decrypt** text messages using the classic Caesar Cipher technique.

---

## 📖 About

The Caesar Cipher is one of the earliest known encryption techniques. It works by shifting each letter of a message a fixed number of positions along the alphabet. This project provides an easy-to-use, menu-driven CLI to encrypt and decrypt messages using a custom shift value.

---

## ✨ Features

- 🔐 Encrypt any message using a custom shift value
- 🔓 Decrypt a message back to its original form
- 🔤 Preserves uppercase and lowercase letters correctly
- ✍️ Leaves numbers, spaces, and special characters unchanged
- 🔁 Menu-driven loop — encrypt/decrypt multiple times without restarting
- ⚠️ Basic input validation for the shift value

---

## ⚙️ How It Works

Each letter is shifted using modular arithmetic so the alphabet wraps around correctly:

**Encryption:**
```
new_char = (char - 'A' + shift) % 26 + 'A'
```

**Decryption:**
```
new_char = (char - 'A' - shift) % 26 + 'A'
```

Non-alphabetic characters (digits, spaces, punctuation) are left unchanged.

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## 🚀 Usage

**1. Clone or download the script**

```bash
git clone https://github.com/prince-jha8533/caesar-cipher.git
cd caesar-cipher
```

**2. Run the script**

```bash
python task1.py
```

**3. Choose an option from the menu**

```
1. Encrypt
2. Decrypt
3. Exit
```

**4. Follow the prompts** to enter your message and shift value.

---

## 💻 Example

```
================================
       CAESAR CIPHER
================================

1. Encrypt
2. Decrypt
3. Exit

Enter your choice: 1
Enter message: Hello World
Enter shift value: 3

Encrypted Message: Khoor Zruog
```

Decrypting `Khoor Zruog` with a shift of `3` returns the original message: `Hello World`.

---

## 📂 Project Structure

```
.
└── task1.py    # Encrypt/decrypt logic + CLI menu
```
## 📄 License

This project is open source and available for personal or educational use.
