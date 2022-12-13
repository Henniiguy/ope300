from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Open the file in read-only mode
with open('/path/to/file', 'rb') as f:
    # Read the file contents
    data = f.read()

# Create a Fernet object using the key
fernet = Fernet(key)

# Encrypt the data
encrypted_data = fernet.encrypt(data)

# Open the file in write-binary mode
with open('/path/to/file', 'wb') as f:
    # Write the encrypted data to the file
    f.write(encrypted_data)
