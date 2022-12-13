import os

# Get the directory path
directory_path = '/path/to/directory'

# Get a list of all files in the directory
files = os.listdir(directory_path)

# Print the full paths of the files
for file in files:
    file_path = os.path.join(directory_path, file)
    print(file_path)
