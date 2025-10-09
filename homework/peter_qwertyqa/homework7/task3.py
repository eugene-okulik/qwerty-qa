array = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9",
    "результат: 2"
]


def get_number(element):
    # сплитим по двоеточию, берем последний элемент, убираем пробел в начале
    return int(element.split(":")[-1][1:])


for line in array:
    # idx = line.index(':') + 2   # ищем двоеточие, берем срез для числа
    # number = int(line[idx:])
    print(get_number(line) + 10)
