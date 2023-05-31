# Declare a class named Book (book), whose objects are created by the command:
#
# book = Book(title, author, pages)
#
# where title is the title of the book (string); author - book author (string);
# pages - number of pages in the book (integer).
#
# Also, when displaying information about an object on the screen with the command:
#
# print(book)
#
# line should be displayed in the format:
#
# 'Book: {title}; {author}; {pages}'
#
# For example:
#
# 'Book: Mumu; Turgenev; 123'
#
# Read lines with information about the book from the input stream with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# (the lines are in order: title, author, pages).
# Create an object of class Book and print its string representation to the console.


class Book:
    def __init__(self, *args):
        self.title = args[0]
        self.author = args[1]
        self.pages = int(args[2])

    def __str__(self):
        return f"Book: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, [input() for _ in range(3)]))
book = Book(*lst_in)
print(book)
