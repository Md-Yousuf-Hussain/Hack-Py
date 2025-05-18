import random
import string

char = string.punctuation + string.digits + string.ascii_letters + " "
char = list(char)
key = char.copy()

# print(f"char: {char}")
# print(f"key: {key}")

random.shuffle(key)

# ---------Encryption--------- #

plain_text = input("Enter a plain text:")
cipher_text = ""

for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]

print(f"Cipher Text: {cipher_text}")

# ---------Decryption--------- #

cipher_text = input("Enter a cipher text:")
plain_text = ""

for letter in cipher_text:
    index = char.index(letter)
    plain += key[index]

print(f"Plain Text: {plain_text}")