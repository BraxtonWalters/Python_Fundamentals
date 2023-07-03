

class Library:
    all_libraries = []
    def __init__(self, name):
        self.name = name
        self.books = []

        Library.all_libraries.append(self)

    def show_books(self):
        if len(self.books) > 0:
            for book in self.books:
                print(book.name)
        else:
            print(f"No books in {self.name} 🤷‍♂️")
