import datetime

with open('input.txt', 'r') as f:
    x = f.readlines()
with open('output.txt', 'w') as f:
    now = datetime.datetime(2024, int(x[0].split('.')[1]), int(x[0].split('.')[0]))
    for line in x[2:]:
        date = datetime.datetime(2024, int(line.split(' ')[1].split('.')[1]), int(line.split(' ')[1].split('.')[0]))
        difference = now - date
        if difference.total_seconds() // (60*60*24) > 3:
            f.write(f'{line.split(' ')[0]}\n')
