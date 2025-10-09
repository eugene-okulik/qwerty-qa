from random import randint, choice

salary = int(input())
bonus = choice([True, False])

if bonus:
    salary += randint(1, 10000)

print(salary)
