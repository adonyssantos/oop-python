class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def in_stock(self):
        if self.copies > 0:
            return f"{self.title} is in stock"
        else:
            return f"{self.title} is not in stock"

    def sell(self):
        if self.copies > 0:
            self.copies -= 1
            return f"{self.title} has been sold"
        else:
            return f"{self.title} is not in stock"

    def display_info(self):
        return f"{self.title} by {self.author} is {self.price} dollars and has {self.pages} pages"


books = [
    Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10),
    Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20),
    Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5),
    Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6),
]

for book in books:
    print(book.display_info())
