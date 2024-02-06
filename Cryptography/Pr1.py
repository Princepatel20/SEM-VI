# Define the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(message, key):
 message = message.upper().replace(" ", "")
 ciphertext = ""
 for letter in message:
 index = alphabet.index(letter)
 new_index = (index + key) % len(alphabet)
 ciphertext += alphabet[new_index]
 return ciphertext
 
def decrypt(ciphertext, key):
 ciphertext = ciphertext.upper().replace(" ", "")
 plaintext = ""
 for letter in ciphertext:
 index = alphabet.index(letter)
 new_index = (index - key) % len(alphabet)
 plaintext += alphabet[new_index]
 return plaintext
def brute_force(ciphertext):
 plaintexts = []
 for key in range(26):
 plaintext = decrypt(ciphertext, key)
  plaintexts.append((plaintext, key))
 return plaintexts
# Example usage
message = "cryptography"
key = 3
ciphertext = encrypt(message, key)
plaintext = decrypt(ciphertext, key)
possible_plaintexts = brute_force(ciphertext)
print("Message:", message)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)
print("Possible plaintexts and keys:")
for p, k in possible_plaintexts:
 print(p, k)
