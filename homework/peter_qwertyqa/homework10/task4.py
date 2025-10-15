PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

items = PRICE_LIST.split()
price_dict = {items[i]: int(items[i + 1][:-1]) for i in range(0, len(items), 2)}

print(price_dict)
