# Declare a DateString class to represent dates whose objects are created by the command:
#
# date = DateString(date_string)
#
# where date_string is a date string in the format:
#
# 'DD.MM.YYYY'
#
# here DD - day (an integer from 1 to 31); MM - month (integer from 1 to 12); YYYY - year (integer from 1 to 3000).
# For example:
#
# date = DateString('26.05.2022')
#
# or
#
# date = DateString('26.5.2022') # non-significant zero may be missing
#
# If the specified date in the string is written incorrectly (not in the format),
# then throw an exception using your own class:
#
# DateError is an exception class inherited from the Exception class.
#
# In the DateString class itself, override the __str__() magic method to form a date string in the format:
#
# 'DD.MM.YYYY'
#
# (insignificant zeros should appear here, for example,
# for the argument '26.5.2022' the string '26.05.2022' should be formed).
#
# Next, the program reads a line from the input stream with the command:
#
# date_string = input()
#
# Your task is to create an object of the DateString class with the date_string argument
# and display the object on the screen with the command:
#
# print(date) # date is an object of class DateString
#
# If an exception occurs, then display a message (without quotes):
#
# 'Invalid date format'


class DateError(Exception):
    pass


class DateString:
    def __init__(self, string):
        data = [int(x) for x in string.split(".")]
        if not 1 <= data[0] <= 31 or not 1 <= data[1] <= 12 or not 1 <= data[2] <= 3000:
            raise DateError("Invalid date format")
        self.day, self.month, self.year = data

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


date_string = "1.2.1812"

try:
    d = DateString(date_string)
    print(d)
except DateError as e:
    print(e)
