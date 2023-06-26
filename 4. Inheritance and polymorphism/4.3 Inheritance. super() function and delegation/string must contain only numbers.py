# Declare a StringDigit class that inherits from the standard str class.
# Objects of the StringDigit class must be created with the command:
#
# sd = StringDigit(string)
#
# where string is a string of numbers (for example, '12455752345950').
# If at least one non-numeric character appears in the string string, then generate an exception with the command:
#
# raise ValueError('string must contain only digits')
#
# Also, in the StringDigit class, you need to redefine the + operator (string concatenation) so that the operations:
#
# sd = sd + '123'
# sd = '123' + sd
#
# created new objects of the StringDigit class (and not of the str class).
# If, when connecting strings, a non-numeric character appears, then throw an exception:
#
# raise ValueError('string must contain only digits')
#
# An example of using the class (do not write these lines in the program):
#
# sd = StringDigit('123')
# print(sd) # 123
# sd = sd + '456' # StringDigit: 123456
# sd = '789' + sd # StringDigit: 789123456
# sd = sd + '12f' # ValueError


class StringDigit(str):
    def __init__(self, string):
        if not string.isdigit():
            raise ValueError("string must contain only numbers")
        super().__init__()

    def __add__(self, other):
        return StringDigit(str(self) + other)

    def __radd__(self, other):
        return StringDigit(other + str(self))


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError
