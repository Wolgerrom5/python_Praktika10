with open('input.txt', 'r') as file:
    f = file.read()

c = f.upper()

with open('output.txt', 'w') as file:
    file.write(c)