def encryptRailFence(text, key)

rail = [['\n' for i in range(len(text))]

for j in range(key)]

dir_down = False

row, col = 0, 0

for i in range(len(text)):

if (row == 0) or (row == key - 1):

dir_down = not dir_down

rail[row][col] = text[i]

col += 1

if dir_down:

row += 1

else:

row -= 1

result = []

for i in range(key):

for j in range(len(text)):

if rail[i][j] != '\n':

result.append(rail[i][j])

return("" . join(result))
def decryptRailFence(cipher, key):

rail = [['\n' for i in range(len(cipher))]

for j in range(key)]

dir_down = None

row, col = 0, 0

for i in range(len(cipher)):

if row == 0:

dir_down = True

if row == key - 1:

dir_down = False

rail[row][col] = '*'

col += 1

if dir_down:

row += 1

else:

row -= 1

index = 0

for i in range(key):

for j in range(len(cipher)):

if ((rail[i][j] == '*') and

(index < len(cipher))):

rail[i][j] = cipher[index]

index += 1
result = []

row, col = 0, 0

for i in range(len(cipher)):

if row == 0:

dir_down = True

if row == key-1:

dir_down = False

if (rail[row][col] != '*'):

result.append(rail[row][col])

col += 1

if dir_down:

row += 1

else:

row -= 1

return("".join(result))

def readFromFile(filename):

with open(filename, 'r') as file:

data = file.read().replace('\n', '')

return data

def writeToFile(filename, data):

with open(filename, 'w') as file:

file.write(data)
if __name__ == "__main__":

# Read plain text from a file

plain_text = readFromFile('plain_text.txt')

print(" Plain Text Fetch")

# Encrypt the plain text

encrypted text = encryptRailFence(plain_text, 3)

# Write the encrypted text to a file

writeToFile('encrypted_text.txt', encrypted_text)

print(" Cipher Text Written")

# Read the encrypted text from the file

encrypted_text = readFromFile('encrypted_text.txt')

# Decrypt the encrypted text

decrypted_text = decryptRailFence(encrypted_text, 3)

# Write the decrypted text to a file

writeToFile('decrypted_text.txt', decrypted_text)

print(" Decrypted Text Written")

# Print the encryption table

print("Encryption Table:")

print("Plain Text : Key : Encrypted Text ")

print(f" {plain_text} : 3 :{encrypted_text} ")
