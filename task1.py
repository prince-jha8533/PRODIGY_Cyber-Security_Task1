# Caesar Cipher
# Task 01 - Encryption and Decryption

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        else:
            result += char

    return result


print("================================")
print("       CAESAR CIPHER")
print("================================")

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        message = input("Enter message: ")

        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        encrypted_message = encrypt(message, shift)

        print("\nEncrypted Message:", encrypted_message)

    elif choice == "2":
        message = input("Enter encrypted message: ")

        try:
            shift = int(input("Enter shift value: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        decrypted_message = decrypt(message, shift)

        print("\nDecrypted Message:", decrypted_message)

    elif choice == "3":
        print("\nProgram ended.")
        break

    else:
        print("\nInvalid choice. Please try again.")