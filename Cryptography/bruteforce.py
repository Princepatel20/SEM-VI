ciphertext = "Rtjoq"

print("Ciphertext:", ciphertext)

for shift in range(1, 27):

  decrypted = ""

  for char in ciphertext:
    if char.isalpha():
      char_code = ord(char)
      char_code = (char_code - ord('A') - shift + 26) % 26 + ord('A')
      decrypted += chr(char_code)
    else:
      decrypted += char

  print("Shift:", shift)
  print("Decrypted:", decrypted)
  print()

print("Done!")
