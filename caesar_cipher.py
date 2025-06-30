def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose (E)ncrypt or (D)ecrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'e':
        print("Encrypted:", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted:", decrypt(message, shift))
    else:
        print("Invalid choice. Please enter E or D.")

if __name__ == "__main__":
    main()
