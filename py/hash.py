import hashlib

# Prompt the user for a string
input_string = input("Enter a string: ")

# Convert the string to a hash value using SHA-256
hash_value = hashlib.sha256(input_string.encode()).hexdigest()

# Print the hash value
print(hash_value)
