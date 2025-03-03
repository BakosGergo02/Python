from random import randint

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_otp(characters):
    with open("otp.txt","w") as f:
        for i in range(characters):
            f.write(str(randint(0,25))+ "\n")
            
def load_otp():
    with open("otp.txt","r") as f:
        contents = f.read().splitlines()
    return contents

def encrypt(message,key):
    ciphertext = ''
    for (position,character) in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character)+int(key[position]))%len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext    
    


def decrypt(ciphertext,key):
    decrypttext = ''
    for (position,character) in enumerate(ciphertext):
        if character not in ALPHABET:
            decrypttext += character
        else:
            decrypted = (ALPHABET.index(character)-int(key[position]))%len(ALPHABET)
            decrypttext += ALPHABET[decrypted]
    return decrypttext    
    



while True:
    message = input("Please enter a message:").lower()
    generate_otp(len(message))
    key = load_otp()
    if message == 'q': break
    encry_message = encrypt(message,key)
    print("Encrypted message:", encry_message)
    decry_message = decrypt(encry_message,key)
    print("Decrypted message:", decry_message)
