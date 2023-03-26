
import subprocess

filename = 'filename.txt'
command = "sed -r 's/[^0-9]*([0-9]+)[^0-9]*/\\1 /g; s/ $//' {}".format(filename)
result = subprocess.check_output(command, shell=True, universal_newlines=True)

# Remove empty lines from the result
result_lines = result.split('\n')
result_lines = [line.strip() for line in result_lines if line.strip()]

# Print the result without empty lines
print('\n'.join(result_lines))


