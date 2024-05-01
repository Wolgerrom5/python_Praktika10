with open('input.txt', 'r') as f:
    file = f.readlines()
    with open('simple/output.txt', 'w') as output:
        for i in range(1, len(file) + 1):
            if i % 2 == 0:
                output.write(file[i-1])