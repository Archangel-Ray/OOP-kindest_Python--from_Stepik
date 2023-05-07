# Declare a TriangleChecker class whose objects could be created with the command:
#
# tr = TriangleChecker(a, b, c)
#
# Here a, b, c are the lengths of the sides of the triangle.
#
# In the TriangleChecker class, you must declare the is_triangle() method, which would return the following codes:
#
# 1 - if at least one side is not a number (not a float or int) or at least one number is less than or equal to zero;
# 2 - the indicated numbers a, b, c cannot be the lengths of the sides of the triangle;
# 3 - sides a, b, c form a triangle.
#
# Parameters a, b, c should be checked in that order.
#
# Read from the input stream a line containing three numbers separated by spaces with the command:
#
# a, b, c = map(int, input().split())
#
# Then, create a tr object of the TriangleChecker class and pass it the read a, b, c values. Call the is_triangle()
# method on the tr object and print the result to the screen (the code it will return).


class TriangleChecker:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def is_triangle(self):
        if type(self.a) not in (float, int) or self.a <= 0 or \
                type(self.b) not in (float, int) or self.b <= 0 or \
                type(self.c) not in (float, int) or self.c <= 0:
            return 1
        if self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
