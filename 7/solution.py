with open('input.txt', 'r') as f:
    number = f.readlines()
with open('input.txt', 'w') as f:
    for i in number:
        if '100' in i:
            i = i.replace('100', '')
        f.write(i)