def decrypt_caesar(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = len(alphabet)

    def decrypt(text, key):
        decrypted_message = ''
        for char in text:
            if char in alphabet:
                decrypted_char = alphabet[(alphabet.index(char)-key)%n]
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message


    for key in range(1, 26):
        decrypted_message = decrypt(ciphertext, key)
        if key == 4:
            print(decrypted_message)

ciphertext = "iqfihhih"
decrypt_caesar(ciphertext)
