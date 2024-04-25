try:
    with open('input.txt', 'r') as f:
        f = f.readlines()
        if len(f) > 0:
            n = int(f[0])
            if len(f) - 1 == n:
                with open('output.txt', 'w') as f:
                    f.write('YES')
            else:
                with open('output.txt', 'w') as f:
                    f.write('NO')
except ValueError:
    with open('output.txt', 'w') as f:
        f.write('ERROR')
