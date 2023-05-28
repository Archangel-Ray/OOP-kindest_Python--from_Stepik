# Declare a DigitRetrieve class to convert data from a string to numbers.
# Objects of this class are created by the command:
#
# dg = DigitRetrieve()
#
# Then, they are supposed to be used, for example, as follows:
#
# d1 = dg('123') # 123 (integer)
# d2 = dg('45.54') # None (not an integer)
# d3 = dg('-56') # -56 (integer)
# d4 = dg('12fg') # None (not an integer)
# d5 = dg('abc') # None (not an integer)
#
# That is, the integers in the string should be cast to the integer data type, and all others to the None value.
#
# Using objects of the DigitRetrieve class, the conversion of numbers from a list of strings should be performed
# as follows:
#
# st = ['123', 'abc', '-56.4', '0', '-5']
# digits = list(map(dg, st)) # [123, None, None, 0, -5]


class DigitRetrieve:
    def __call__(self, string):
        if string.isdigit() or string[0] == "-" and string[1:].isdigit():
            return int(string)
        return None


dg = DigitRetrieve()
st = ['123', 'abc', '-56.4', '0', '-5']
digits = list(map(dg, st))
print(digits)
