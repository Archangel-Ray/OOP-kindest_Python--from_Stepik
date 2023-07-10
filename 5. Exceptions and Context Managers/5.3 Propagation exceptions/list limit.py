# The program reads numeric data from the input stream using the command:
#
# digits = list(map(float, input().split()))
#
# This data should be represented as an object of the TupleLimit class. The class itself must be inherited
# from the tuple class, and its objects must be created by the command:
#
# tl = TupleLimit(lst, max_length)
#
# where lst is a collection (list or tuple) of data; max_length - the maximum allowed length of the TupleLimit
# collection. If the length of lst exceeds the value of max_length, then an exception should be thrown with the command:
#
# raise ValueError('the number of elements in the collection exceeds the specified limit')
#
# In the TupleLimit class itself, override the magic methods __str__() and __repr__() to display an object
# of the TupleLimit class as a string from the lst data set separated by a space. For example:
#
# '1.0 2.5 -5.0 11.2'
#
# Create an object of the TupleLimit class in the program for the read data digits and the parameter max_length = 5.
# Display the object on the screen if it was successfully created.
# Otherwise, print the message of the handled exception.


class TupleLimit(tuple):
    def __new__(cls, iterable, maximum):
        if len(iterable) > maximum:
            raise ValueError("the number of elements in the collection exceeds the specified limit")

        return super().__new__(cls, iterable)

    def __str__(self):
        return ' '.join(map(str, self))


digits = list(map(float, input().split()))

try:
    test = TupleLimit(digits, 5)
    print(test)
except ValueError as e:
    print(e)
