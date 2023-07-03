class Book:
    all_books = []
    
    def __init__(self, name, year, num_of_pages):
        self.name = name
        self.year = year
        self.num_of_pages = num_of_pages

        Book.all_books.append(self)