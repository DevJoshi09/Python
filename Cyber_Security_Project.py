# substitution ciphertext (Type -> MonoAlphabetic cipher)

import string
import random

# string 
chars = " " + string.punctuation + string.digits + string.ascii_lowercase

# type cast string to list
chars = list(chars)
key = chars.copy()

# shuflle key every time when generating cipher text
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"keys : {key}")


# Encryption

plain_text = input("Enter a message to encrypt : ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Plain_Text : {plain_text}")
print(f"Cipher_Text: {cipher_text}")


# Decrytion
cipher_text = input("Enter a message to decrypt : ")
plain_text = " "
for letter in cipher_text:

    index = key.index(letter)
    plain_text += chars[index]


print(f"Cipher_Text: {cipher_text}")
print(f"Plain_Text : {plain_text}")

# --------------------------------------------------------------------------------------------------------------

# ceasor cipher

characters = string.ascii_lowercase
print(characters)

# Encryption 

cipher_text = ""
plain_text = input("Enter a message : ").lower()

shift = int(input("Enter shifts : "))

for letter in plain_text :

    index = characters.index(letter)
    ct_index = (index + shift) % 26
    cipher_text += characters[ct_index]


print(f"cipher text : {cipher_text}")
# print(plain_text)

# Decryption

plain_text = ""
cipher_text = input("Enter a cipher text : ").lower()

shift = int(input("Enter shifts : "))

for letter in cipher_text :

    index = characters.index(letter)
    pt_index = (index + 26 - shift) % 26
    plain_text += characters[pt_index]


print(f"plain text : {plain_text}")