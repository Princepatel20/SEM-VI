plaintext = "Prince"

print("Plaintext: ", plaintext)

for shift in range(1, 27):
  
  encrypted = ""
  for char in plaintext:
    if char.isalpha():
      char_code = ord(char)
      char_code = (char_code - ord('A') + shift) % 26 + ord('A')
      encrypted += chr(char_code)
    else:
      encrypted += char

  print("Shift: ", shift)
  print("Encrypted: ", encrypted)
  print()

print("Done!")
