my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [10, 20, 30, 40, 50],
    'dict': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'},
    'set': {100, 200, 300, 400, 500}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(60)
del my_dict['list'][1]
# print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = 123
my_dict['dict'].pop(2)
# print(my_dict['dict'])

my_dict['set'].add(600)
my_dict['set'].remove(100)
# print(my_dict['set'])

print(my_dict)
