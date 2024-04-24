with open('input.txt', 'r') as f:
    f = f.readlines()
c = (line for line in f if len(line) > 21)
with open('output.txt', 'w') as f:
    for line in c:
        f.write(line)
