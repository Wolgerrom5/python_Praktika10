with open('input.txt', 'r') as f:
    f = f.readlines()
c = ''.join(line[0] for line in f)
with open('output.txt', 'w') as f:
    f.write(c)
