# Declare a WordString class whose objects are created by commands:
#
# w1 = WordString()
# w2 = WordString(string)
#
# where string is the string to be passed. For example:
#
# words = WordString('Python OOP course')
#
# Implement the following functionality for objects of this class:
#
# len(words) - should return the number of words in the passed string (words are separated by one or more spaces);
# words(indx) - the word must be returned by its index
# (indx is the ordinal number of the word in the string, starting from 0).
#
# Also implement a property object in the WordString class:
#
# string - to send and read a string.
#
# An example of using the WordString class (these lines do not need to be written in the program):
#
# words = WordString()
# words.string = "Python OOP course"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Number of words: {n}; first word: {first}")


class WordString:
    def __init__(self, string=""):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, str):
        self.__string = str

    def __len__(self):
        return len(self.__string.split())

    def __call__(self, integer):
        return self.__string.split()[integer]


words = WordString()
words.string = "Python OOP course"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Number of words: {n}; first word: {first}")
