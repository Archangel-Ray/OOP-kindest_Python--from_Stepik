# You are instructed to create a book accounting program (library).
# To do this, you need to declare two classes in the program:
#
# Lib - to represent the library as a whole;
# Book - to describe a single book.
#
# Objects of the Book class must be created with the command:
#
# book = Book(title, author, year)
#
# where title - book title (string); author - book author (string); year - year of publication (integer).
#
# Objects of the Lib class are created by the command:
#
# lib = lib()
#
# Each object must contain a local public attribute:
#
# book_list - a link to a list of books (objects of the Book class). The list is initially empty.
#
# Also objects of the Lib class must work with the following operators:
#
# lib = lib + book # adding a new book to the library
# lib += book
#
# lib = lib - book # deleting the book book from the library (deletion occurs on the previously created book object
# of the Book class)
# lib -= book
#
# lib = lib - indx # deleting a book by its serial number (index: counting starts from zero)
# lib -= indx
#
# When implementing the binary operators + and -, you do not need to create copies of libraries
# (objects of the Lib class).
#
# Also, the following function should work with objects of the Lib class:
#
# n = len(lib) # n is the number of books
#
# which returns the number of books in the library.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def del_book(self, book):
        self.book_list.remove(book)

    def pop_book(self, indx):
        self.book_list.pop(indx)

    def __add__(self, other):
        self.add_book(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) == Book:
            self.del_book(other)
            return self
        if type(other) == int:
            self.pop_book(other)
            return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.book_list)


lib = Lib()
Bulgakov = Book("Master and Margarita", "M.A. Bulgakov", 1966)
Akunin = Book("Azazel", "Boris Akunin", 1988)
Glukhovsky = Book("Metro 2033", "Dmitry Glukhovsky", 2005)
Sorokin = Book("Day of the Oprichnik", "Vladimir Sorokin", 2010)
Dostoevsky = Book("Crime and Punishment", "Fedor Dostoevsky", 1866)
lib = lib + Bulgakov
lib = lib + Akunin
lib += Glukhovsky
lib += Sorokin
print(len(lib))
lib += Dostoevsky
lib = lib - Akunin
lib -= Sorokin
lib = lib - 1
lib -= 0
print(len(lib))
