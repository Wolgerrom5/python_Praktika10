with open('input.txt', 'r') as f:
    f = f.readlines()
c = []
for i in f:
    if i[0] == 'a' or i[0] == 'A':
        c += i
with open('output.txt', 'w') as f:
    for i in c:
        f.write(i)