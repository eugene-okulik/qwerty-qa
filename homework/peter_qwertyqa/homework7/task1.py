import random


x = random.randint(1, 10)

guess_num = int(input())

while guess_num != x:
    print("попробуйте снова")
    guess_num = int(input())

print("Поздравляю! Вы угадали!")
