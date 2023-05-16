# Declare a Book class with the following set of setters and getters:
#
# set_title(self, title) - writing the title value to the local private property __title of Book class objects;
# set_author(self, author) - setting the local private property __author of objects of class Book with the value author;
# set_price(self, price) - writing the value of price to the local private property __price of Book class objects;
# get_title(self) - getting the value of the local private property __title of Book class objects;
# get_author(self) - getting the value of the local private property __author of Book class objects;
# get_price(self) - getting the value of the local private property __price of Book class objects;
#
# Book class objects are supposed to be created by the command:
#
# book = Book(author, title, price)
# At the same time, private local properties should be created in each object:
#
# __author - a string with the author's name;
# __title - a string with the title of the book;
# __price - an integer with the price of the book.


class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


book_1 = Book("Tolstoy", "War and Peace", 100)
book_1.set_author("L. N. Tolstoy")
book_1.set_title("Anna Karenina")
book_1.set_price(200)
print(f'{book_1.get_author()} - "{book_1.get_title()}" (${book_1.get_price()})')
