with open('input.txt', 'r') as file:
    lines = file.readlines()
file_2= []
for i in  lines:
    if i.strip().startswith('a') or i.strip().startswith('A'):
        file_2.append(i.strip())

with open('output.txt', 'w') as output_file:
    for line in file_2:
        output_file.write(line + '\n')
