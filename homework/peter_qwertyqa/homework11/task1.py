class Book:
    material = "бумага"
    hasText = True

    def __init__(self, title, author, page_amount, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.page_amount = page_amount
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_info(self):
        book_info = (f"Название: {self.title}, Автор: {self.author}, страниц: "
                     f"{self.page_amount}, материал: {self.material}")
        if self.is_reserved:
            return f"{book_info}, зарезервирована"
        else:
            return book_info


books = [
    Book("Идиот", "Достоевский", 500, "346578346836"),
    Book("Война и мир", "Толстой", 1200, "4576895769"),
    Book("1984", "Оруэлл", 350, "11111111"),
    Book("Мастер и Маргарита", "Булгаков", 420, "09845784"),
    Book("Гарри Поттер", "Роулинг", 450, "88888883"),
]

books[4].is_reserved = True

for b in books:
    print(b.print_info())


class StudentBook(Book):
    def __init__(self, title, author, page_amount, isbn, subject,
                 school_class, has_tasks, is_reserved=False):
        super().__init__(title, author, page_amount, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = has_tasks

    def book_info(self):
        book_info = (f"Название: {self.title}, Автор: {self.author}, "
                     f"страниц: {self.page_amount}, предмет: {self.subject}, "
                     f"класс: {self.school_class}")
        if self.is_reserved:
            return f"{book_info}, зарезервирована"
        else:
            return book_info


student_books = [
    StudentBook("Алгебра", "Иванов", 200, "1111111111",
                "Математика", 9, True),
    StudentBook("История России", "Петров", 300, "2222222222",
                "История", 10, True),
    StudentBook("География", "Сидоров", 250, "3333333333",
                "География", 8, False),
]

student_books[2].is_reserved = True

print("\n")
for sb in student_books:
    print(sb.book_info())
