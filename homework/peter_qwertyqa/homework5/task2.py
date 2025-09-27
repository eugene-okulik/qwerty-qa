array = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

for line in array:
    idx = line.index(':') + 2   # ищем двоеточие, берем срез для числа
    number = int(line[idx:])
    print(number + 10)
