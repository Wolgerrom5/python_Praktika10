with open('input.txt', 'r') as f:
    f = f.read()
c = f.upper()
with open('output.txt', 'w') as f:
    f.write(c)