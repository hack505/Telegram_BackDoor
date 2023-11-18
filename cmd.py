import subprocess

# Command you want to execute
cmd_command = 'ls'  # You can replace this with any CMD command you want to run

# Run the command and capture the output
result = subprocess.run(
    cmd_command, stdout=subprocess.PIPE, text=True, shell=True)

# Print the output
print(result.stdout)
