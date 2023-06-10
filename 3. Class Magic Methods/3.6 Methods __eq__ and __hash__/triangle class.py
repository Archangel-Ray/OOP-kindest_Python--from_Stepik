# Declare a class named Triangle whose objects are created by the command:
#
# tr = Triangle(a, b, c)
#
# where a, b, c are the lengths of the sides of the triangle (numbers: integer or real). In the Triangle class,
# declare the following data descriptors:
#
# a, b, c - for writing and reading the lengths of the sides of a triangle.
#
# When writing a new value, you need to check that a positive number (integer or real) is assigned. Otherwise,
# an exception is thrown with the command:
#
# raise ValueError("triangle side lengths must be positive numbers")
#
# You also need to check that all three sides a, b, c can form sides of a triangle.
# That is, the following conditions must be met:
#
# a < b+c; b < a+c; c < a+b
#
# Otherwise, an exception is thrown with the command:
#
# raise ValueError("The specified lengths cannot form a triangle")
#
# Finally, the following functions must be performed on objects of the Triangle class:
#
# len(tr) - returns the perimeter of the triangle, reduced to an integer value using the int() function;
# tr() - returns the area of ​​a triangle (can be calculated using Heron's formula:
# s = sqrt(p * (p-a) * (p-b) * (p-c)), where p is the half-perimeter of the triangle).
from math import sqrt


class ValueDis:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            return ValueError("the lengths of the sides of a triangle must be positive numbers")
        setattr(instance, self.name, value)


class Triangle:
    a = ValueDis()
    b = ValueDis()
    c = ValueDis()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __check(a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == "a" and not self.__check(value, self.b, self.c)) or \
                (key == "b" and not self.__check(self.a, value, self.c)) or \
                (key == "c" and not self.__check(self.a, self.b, value)):
            raise ValueError("with the specified lengths it is impossible to form a triangle")

        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c) if self.a and self.b and self.c else None

    def __call__(self):
        a, b, c = self.a, self.b, self.c
        if not (a, b, c):
            return
        p = len(self) / 2
        return sqrt(p * (p-a) * (p-b) * (p-c))


triangle = Triangle(5, 5, 5)
print(len(triangle))
print(triangle())
