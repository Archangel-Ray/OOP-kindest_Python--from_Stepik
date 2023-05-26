# Declare in the program the class Dimensions (dimensions) with attributes:
#
# MIN_DIMENSION = 10
# MAX_DIMENSION = 1000
#
# Each object of class Dimensions must be created with the command:
#
# d3 = Dimensions(a, b, c) # a, b, c - overall dimensions
#
# and contain local attributes:
#
# __a, __b, __c - overall dimensions (integer or real numbers).
#
# To work with these local attributes, the following property objects should be registered in the Dimensions class:
#
# a, b, c - to change and read the corresponding local attributes __a, __b, __c.
#
# When changing the values ​​of __a, __b, __c, you should check that the assigned value is a number in the range
# [MIN_DIMENSION; MAX_DIMENSION]. If it is not, then the new value is not assigned (ignored).
#
# Use the magic methods in this lesson to disable the creation of local MIN_DIMENSION and MAX_DIMENSION attributes
# on Dimensions objects. When you try to do this, throw an exception:
#
# raise AttributeError('The MIN_DIMENSION and MAX_DIMENSION attributes cannot be changed.')
#
# An example of using the class (you do not need to write these lines in the program):
#
# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10 # AttributeError exception


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __setattr__(self, key, value):
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Changing the MIN_DIMENSION and MAX_DIMENSION attributes is not allowed.")
        if type(value) in (int, float) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            super().__setattr__(key, value)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.a = 10
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # AttributeError exception
print(d.__dict__)
