try:
    with open('input.txt', 'r') as f:
        a, b, c = map(float, f.readline().split())
    with open('output.txt', 'w') as f:
        result = (a / b) + c
        f.write(str(result))
except ZeroDivisionError:
    print('division by 0')
except ValueError:
    print('data error')
