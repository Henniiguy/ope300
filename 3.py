import subprocess

# Run the netstat command and capture the output
output = subprocess.check_output(["netstat", "-an"])

# Convert the output to a string and split it into lines
output_str = output.decode('utf-8')
lines = output_str.split('\n')

# Loop through the lines and print the ones that start with "tcp"
for line in lines:
    if line.startswith('tcp'):
        print(line)
