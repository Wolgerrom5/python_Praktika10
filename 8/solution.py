with open('input.txt', 'r') as f:
    file = f.readlines()
steps = [0] * 12
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12):
    for n in range(days[i]):
        steps[i] += int(file[i * 31 + n])

average = [step / day for step, day in zip(steps, days)]

with open('output.txt', 'w') as fi:
    for step in average:
        fi.write(str(step))
