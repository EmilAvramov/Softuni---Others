class Book:
    def __init__(self, _name: str, _author: str, _pages: int) -> None:
        self.name = _name
        self.author = _author
        self.pages = int(_pages)


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
