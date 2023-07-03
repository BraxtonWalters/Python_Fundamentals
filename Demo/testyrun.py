# class Employee:
#     def set_name(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

# print(Employee.set_name)
# bobby = Employee()
# print("-" * 80)
# print(bobby.set_name)
# print("-" * 80)
# print("-" * 80)


# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def user_info(self):
#         print(self.first_name)
#         print(self.last_name)
#         return self

#     def info(self):
#         print(["first_name", "last_name"])
#         return self

#     def new_fn(self, name):
#         self.first_name = name
#         return self

# robby = Person("Robby", "Townson")
# robby.new_fn("Bobby")
# robby.info().user_info()







from testylibrarian import Library
from testygirl import Book

braxton_library = Library("Braxton Library")

bk1 = book("To Kill a Mockingbird", 1960, 281)
bk1 = book("1984", 1949, 328)
bk1 = book("The Catcher in the Rye", 1951, 277)
bk1 = book("The Great Gatsby", 1925, 180)
bk1 = book("Pride and Prejudice", 1813, 279)
bk1 = book("The Hobbit", 1937, 310)
bk1 = book("The Lord of the Rings", 1955, 1200)
bk1 = book("Harry Potter and the Philosopher's Stone", 1997, 223)
bk1 = book("The Da Vinci Code", 2003, 689)
bk1 = book("The Hunger Games", 2008, 374)

# print(braxton_library)
# print(Library.all_libraries)

braxton_library.show_books()