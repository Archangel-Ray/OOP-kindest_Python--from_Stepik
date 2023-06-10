# From the input stream, you need to read the list of lines with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Each line contains information about the tutorial in the format:
#
# 'Title; author; year of publication'
#
# For example:
#
# Python; Balakirev S.M.; 2020
# Python OOP; Balakirev S.M.; 2021
# Python OOP; Balakirev S.M.; 2022
# Python; Balakirev S.M.; 2021
#
# It is necessary to represent each of these lines with an object of the BookStudy class,
# which are created by the command:
#
# bs = BookStudy(name, author, year)
#
# where name is the name of the manual (string); author - author of the tutorial (string);
# year - year of publication (integer). The same public local attributes must be in BookStudy class objects.
#
# For each object, implement hash calculation on two attributes: name and author (case insensitive).
#
# Form a list of lst_bs from BookStudy class objects based on the read lines (lst_in list).
# After that, determine the number of books with unique hashes.
# Save this number through the unique_books variable (integer).


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = [
    "Python; Balakirev S.M.; 2020",
    "Python OOP; Balakirev S.M.; 2021",
    "Python OOP; Balakirev S.M.; 2022",
    "Python; Balakirev S.M.; 2021"
]
lst_bs = []
for string in lst_in:
    attributes = list(map(str.strip, string.split(";")))
    attributes[-1] = int(attributes[-1])
    lst_bs.append(BookStudy(*attributes))
unique_books = len(set([hash(x) for x in lst_bs]))
print(unique_books)
