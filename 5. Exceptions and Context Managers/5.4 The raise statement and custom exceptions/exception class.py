# In your program, declare an exception class named PrimaryKeyError that is derived from the Exception base class.
# Objects of the PrimaryKeyError class must be created with the commands:
#
# e1 = PrimaryKeyError() # Primary key must be a non-negative integer
# e2 = PrimaryKeyError(id='abc') # Primary key value id = abc is invalid
# e3 = PrimaryKeyError(pk='123') # Primary key value pk = 123 is invalid
#
# The first variant of the command should generate an error message 'Primary key must be a non-negative integer'.
# For the second option:
#
# 'Primary key value id = id is invalid'
#
# And at the third:
#
# 'Primary key value pk = pk is invalid'
#
# These messages should be generated when displaying objects of the PrimaryKeyError class, for example:
#
# print(e2) # Primary key value id = abc is invalid
#
# Then, throw this exception with id = -10.5, handle it, and display the exception object on the screen.


class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if "id" not in kwargs and "pk" not in kwargs:
            self.message = "The primary key must be a non-negative integer"
        else:
            key, value = tuple(kwargs.items())[0]
            self.message = f"Primary key value {key} = {value} is invalid"

    def __str__(self):
        return self.message


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
