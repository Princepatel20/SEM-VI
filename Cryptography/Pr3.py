alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

filler = "X"

def create matrix(key):

 key = "“. join(dict.fromkeys(key.upper()))

 key += "“. join([letter for letter in alphabet if letter not in key])

 matrix = [key[i:i+5] for i in range(0, len(key), 5)]

 return matrix

def find_position(letter, matrix):

 for i, row in enumerate(matrix):

 for j, col in enumerate(row):

 if letter == col:

 return i, j

def encrypt_pair(pair, matrix):

 i1, j1 = find_position(pair[0], matrix)

 i2, j2 = find_position(pair[1], matrix)

 if i1 == i2: # Same row

 return matrix[i1][(j1 + 1) % 5] + matrix[i2][(j2 + 1) % 5]

 elif j1 == j2: # Same column

 return matrix[(i1 + 1) % 5][j1] + matrix[(i2 + 1) % 5][j2]

 else: # Different row and column
return matrix[i1][j2] + matrix[i2][j1]

def decrypt_pair(pair, matrix):

 i1, j1 = find_position(pair[0], matrix)

 i2, j2 = find_position(pair[1], matrix)

 if i1 == i2: # Same row

 return matrix[i1][(j1 - 1) % 5] + matrix[i2][(j2 - 1) % 5]

 elif j1 == j2: # Same column

 return matrix[(i1 - 1) % 5][j1] + matrix[(i2 - 1) % 5][j2]

 else: # Different row and column

 return matrix[i1][j2] + matrix[i2][j1]

def encrypt_message(message, key):

 matrix = create_matrix(key)

 message = message.upper().replace(" ", "")

 pairs = [message[i:i+2] for i in range(0, len(message), 2)]

 if len(pairs[-1]) == 1:

 pairs[-1] += filler

 encrypted = [encrypt_pair(pair, matrix) for pair in pairs]

 return "".join(encrypted)

def decrypt_message(message, key):

 matrix = create_matrix(key)

 message = message.upper().replace(" ", "")

 pairs = [message[i:i+2] for i in range(0, len(message), 2)]

 decrypted = [decrypt_pair(pair, matrix) for pair in pairs]

 return "".join(decrypted)

# Example usage

key = "playfair"
message = "Hello World 2024"

encrypted = encrypt_message(message, key)

decrypted = decrypt_message(encrypted, key)

print("Message:", message)

print("Encrypted:", encrypted)

print("Decrypted:", decrypted)
