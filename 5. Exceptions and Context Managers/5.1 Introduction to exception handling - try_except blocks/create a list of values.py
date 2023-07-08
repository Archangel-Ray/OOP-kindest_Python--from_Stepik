# In the program, some data is entered in one line separated by a space, for example:
#
# '1 -5.6 True abc 0 23.56 hello'
#
# This data is space-separated and presented as a list of strings:
#
# lst_in = input().split()
#
# Your task is to form a new list named lst_out, in which strings with integers will be represented as integers
# (type int), strings with real numbers as real numbers (type float), and the rest of the data will be unchanged.
#
# For example:
#
# lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello'] # after processing input string '1 -5.6 True abc 0 23.56 hello'
#
# You should implement this task using the map() function and declaring a helper function with an exception handling
# mechanism to directly convert data to integers or real numbers.


lst_in = input("write something: ").split()


def is_digit(value):
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            return value


lst_out = list(map(is_digit, lst_in))
print(lst_out)
