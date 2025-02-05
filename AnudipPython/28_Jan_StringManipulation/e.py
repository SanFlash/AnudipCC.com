def caesar_cipher_decoder(cipher, shift):
    decoded = ""
    for char in cipher:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decoded += chr((ord(char) - start - shift) % 26 + start)
        else:
            decoded += char
    return decoded

cipher_text = "dwwdfn"
shift_value = 3
print(caesar_cipher_decoder(cipher_text, shift_value))
