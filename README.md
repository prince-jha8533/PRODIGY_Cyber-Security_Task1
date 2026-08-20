# Caesar Cipher

A simple command-line tool to encrypt and decrypt text using the classic Caesar Cipher technique.

## About

The Caesar Cipher is one of the earliest known encryption techniques. It works by shifting each letter in the message a fixed number of positions down (or up) the alphabet. This project implements both encryption and decryption with an interactive menu-driven interface.

## Features

- 🔐 Encrypt any text message with a custom shift value
- 🔓 Decrypt messages back to their original form
- 🔤 Preserves uppercase and lowercase letters correctly
- ✍️ Leaves numbers, spaces, and special characters unchanged
- 🔁 Loop-based menu so you can encrypt/decrypt multiple times without restarting
- ⚠️ Basic input validation for the shift value

## How It Works

Each letter in the message is shifted by `shift` positions in the alphabet, wrapping around using modulo 26:

- **Encryption:** `new_char = (char - 'A' + shift) % 26 + 'A'`
- **Decryption:** `new_char = (char - 'A' - shift) % 26 + 'A'`

Non-alphabetic characters (digits, punctuation, spaces) are left as they are.

## Requirements

- Python 3 (no external libraries needed)

## Usage

1. Clone this repository or download `task1.py`.
2. Run the script:

   ```bash
   python task1.py
   ```

3. Choose an option from the menu:

   ```
   1. Encrypt
   2. Decrypt
   3. Exit
   ```

4. Follow the prompts to enter your message and shift value.

## Example

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

## Project Structure

```
.
└── task1.py    # Main script with encrypt/decrypt logic and CLI menu
```
