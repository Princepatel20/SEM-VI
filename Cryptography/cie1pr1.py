def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char

    if mode == "decrypt":
        shift = -shift
    return result


def brute_force(ciphertext):
    for i in range(26):
        print(f"Shift {i}: {caesar_cipher(ciphertext, i, 'decrypt')}")


if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    shift = int(input("Enter shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ")

    if mode == "encrypt":
        ciphertext = caesar_cipher(plaintext, shift, mode)
        print(f"Ciphertext: {ciphertext}")
    elif mode == "decrypt":
        ciphertext = caesar_cipher(plaintext, shift, mode)
        print(f"Decrypted text: {ciphertext}")
    elif mode == "brute":
        ciphertext = caesar_cipher(plaintext, shift, "encrypt")
        brute_force(ciphertext)
    else:
        print("Invalid mode")
