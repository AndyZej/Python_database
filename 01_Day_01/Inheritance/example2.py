class Book:
    def __init__(self, title: str, author: str, price: float):
        self.title = title
        self.author = author
        self.price = price

    def say_hi(self):
        print("Hello Iam BOOK")

class File:
    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

    def say_hi(self):
        print("Hello Iam FILE")

class EBook(Book, File):
    def __init__(self, title: str, author: str, price: float, name: str, size: float):
        File.__init__(self, name, size)
        Book.__init__(self, title, author, price)

    def say_hi(self):
        Book.say_hi(self)
        File.say_hi(self)

ebook = EBook("Ebook", "autor", 22, "name", 12)
ebook.say_hi()
print(EBook.__mro__)