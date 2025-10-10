from sys import set_int_max_str_digits

# Без этого конфига лимит цифр для integer был превышен (4300 максимум)
set_int_max_str_digits(100_000)


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fib_gen()

for i in range(1, 100_001):
    number = next(gen)
    # print(i, number)
    if i in [5, 200, 1000, 100_000]:
        print(i, ": ", number)
