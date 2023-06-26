# You have previously used method delegation when you called the base class initializer through the super() function.
# Most often, delegation in Python is associated with calling magic methods of base classes (since their names
# cannot be changed). Let's do this example.
#
# Declare in the program a base class named Book, whose objects are created by the command:
#
# book = Book(title, author, pages, year)
#
# where title - book title (string); author - book author (string); pages - number of pages (integer);
# year - year of publication (integer). In each object of the Book class, the corresponding local attributes
# should be formed: title, author, pages, year.
#
# Declare a DigitBook child class from the Book class whose objects are created by the command:
#
# db = DigitBook(title, author, pages, year, size, frm)
#
# where additional parameters size - book size in bytes (integer);
# frm - book format (string: 'pdf', 'doc', 'fb2', 'txt').
# Each object of the DigitBook class must contain the corresponding local attributes:
# title, author, pages, year, size, frm.
#
# The initialization of the local attributes title, author, pages, year must be performed in the Book base class,
# and the size, frm parameters are initialized in the DigitBook child class.


class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


book = DigitBook("War and Peace", "L.N. Tolstoy", 1300, 1873, 31238, "pdf")
print(book.__dict__)
