class Flowers:
    def __init__(self, lifetime, freshness, color, stem_length, cost):
        self.lifetime = lifetime
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.cost = cost

    def __str__(self):
        return (f"Время жизни: {self.lifetime} дн., "
                f"Свежесть: {self.freshness}%, "
                f"Цвет: {self.color}, "
                f"Длина стебля: {self.stem_length} см, "
                f"Цена: {self.cost} руб.")


class Rose(Flowers):
    def __init__(self, lifetime, freshness, color, stem_length, cost):
        super().__init__(lifetime, freshness, color, stem_length, cost)


class Lily(Flowers):
    def __init__(self, lifetime, freshness, color, stem_length, cost):
        super().__init__(lifetime, freshness, color, stem_length, cost)


flowers = [
    Rose(12, 14, "red", 50, 250),
    Rose(80, 10, "rose", 70, 150),
    Lily(20, 30, "white", 20, 500),
    Rose(3, 30, "red", 20, 100)
]

print(flowers[0].cost)


class Bouquet:
    def __init__(self, flowers_list):
        self.flowers = flowers_list
        self.cost = sum(f.cost for f in flowers)

    # Считаем время жизни букета
    def lifetime(self):
        return sum(f.lifetime for f in self.flowers) / len(self.flowers)

    # Сортируем сразу по любому из параметров
    def sort_by(self, parameter):
        self.flowers.sort(key=lambda f: getattr(f, parameter))

    # Выводим содержимое букета в аутпут
    def __str__(self):
        flowers_str = "\n".join(str(flower) for flower in self.flowers)
        return flowers_str

    # Ищем цветок по любому из параметров
    def find_by_param(self, parameter, target_param):
        res = []
        for f in self.flowers:
            if getattr(f, parameter) == target_param:
                res.append(f)
        if res:
            return Bouquet(res)
        else:
            return None


b = Bouquet(flowers)

print(f"Стоимость букета: {b.cost}")

# Время жизни букета
print(f"Время жизни букета: {b.lifetime()}")

b.sort_by("lifetime")
print("\n --- Сортировка цветов в букете по времени жизни ---\n")
print(b)

b.sort_by("freshness")
print("\n --- Сортировка цветов в букете по свежести --- \n")
print(b)

# Поиск цветков в букете по цвету
print("\n --- Поиск цветков в букете по цвету --- \n")
print(b.find_by_param("color", "red"))

# Поиск цветков в букете по времени жизни
print("\n --- Поиск цветков в букете по времени жизни --- \n")
print(b.find_by_param("lifetime", 12))
print(b.find_by_param("lifetime", 150))
