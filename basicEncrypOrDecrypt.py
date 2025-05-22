import random
import string

# Generate the character sets and key mapping
char = list(string.punctuation + string.digits + string.ascii_letters + " ")
key = char.copy()
random.shuffle(key)

# Encryption function
def encrypt(text):
    cipher_text = ""
    for letter in text:
        if letter in char:
            index = char.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  # Leave unknown characters unchanged
    return cipher_text

# Decryption function
def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += char[index]
        else:
            plain_text += letter  # Leave unknown characters unchanged
    return plain_text

# Main switch menu
def main():
    print("Choose an option:")
    print("1. Encrypt text")
    print("2. Decrypt text")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text = input("Enter plain text: ")
        encrypted = encrypt(text)
        print(f"Encrypted Text: {encrypted}")
    elif choice == '2':
        cipher = input("Enter cipher text: ")
        decrypted = decrypt(cipher)
        print(f"Decrypted Text: {decrypted}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
