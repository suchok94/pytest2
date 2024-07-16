class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def remove_book(self, book):
        if book in self.books:
            self.books[book] -= 1
            if self.books[book] == 0:
                del self.books[book]
        else:
            print("Book not found")

    def find_book(self, book):
        return self.books.get(book, 0) > 0

library = Library()
print(library.books)
library.add_book("qwe")

library.add_book("qwe")
print(library.books)