with open('input.txt', 'r') as file:
    data = file.read()

data_case = data.upper()

with open('output.txt', 'w') as file:
    file.write(data_case)