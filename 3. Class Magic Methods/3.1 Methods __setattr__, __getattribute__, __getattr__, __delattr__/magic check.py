# Declare a Book class to represent information about a book. Objects of this class must be created with the commands:
#
# book = Book()
# book = Book(title, author, number of pages, year of publication)
#
# Each object of the Book class should automatically generate the following local properties:
#
# title - book title (string, empty string by default);
# author - author of the book (string, empty string by default);
# pages - number of pages (integer, default 0);
# year - year of publication (integer, default 0).
#
# Declare the __setattr__ magic method in the Book class to check the types of data assigned to the local properties
# title, author, pages, and year. If the types do not match the local attribute (for example, title should refer
# to a string and pages to an integer), then throw an exception with the command:
#
# raise TypeError('Invalid type of data being assigned.')
#
# Create a book object of class Book for the book in the program:
#
# author: Sergey Balakirev
# title: Python OOP
# pages: 123
# year: 2022


class Book:
    args_dic = {"title": str, "author": str, "pages": int, "year": int}

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.args_dic and self.args_dic[key] == type(value):
            super().__setattr__(key, value)
        else:
            raise TypeError("Wrong data type assigned.")


book = Book("Python OOP", "Sergey Balakirev", 123, 2022)
