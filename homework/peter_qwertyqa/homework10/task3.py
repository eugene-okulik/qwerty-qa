def operation_manager(func):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif second < first:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            operation = '+'
        return func(first, second, operation)
    return wrapper


@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    return None


a, b = map(int, input().split())
print(calc(a, b))
