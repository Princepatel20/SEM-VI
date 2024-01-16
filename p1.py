def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()

            # Shift the character
            char_code = ord(char)
            char_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a')

            result += chr(char_code)
        else:
            # If the character is not a letter, leave it unchanged
            result += char

    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

# Example usage:
plaintext = "Prince"
shift_value = 3
encrypted_text = caesar_cipher(plaintext, shift_value)
decrypted_text = caesar_decipher(encrypted_text, shift_value)

print("Original Text:   ", plaintext)
print("Encrypted Text:  ", encrypted_text)
print("Decrypted Text:  ", decrypted_text)
