import os

# get the metadata for a file
file_path = "/path/to/file.txt"
metadata = os.stat(file_path)

# access the metadata using attributes
print("File size:", metadata.st_size)
print("Creation time:", metadata.st_ctime)
print("Last access time:", metadata.st_atime)
print("Last modification time:", metadata.st_mtime)
