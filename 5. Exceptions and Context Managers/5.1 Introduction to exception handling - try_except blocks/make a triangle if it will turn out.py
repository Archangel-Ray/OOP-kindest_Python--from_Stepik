# Declare the Triangle class in the program, the objects of which are created by the command:
#
# tr = Triangle(a, b, c)
#
# where a, b, c are the lengths of the sides of the triangle (any positive numbers). In each object
# of the Triangle class, local attributes _a, _b, _c with the corresponding values ​​must be formed.
#
# If at least one value a, b, c is passed a non-numeric value, or less than or equal to zero,
# then an exception should be generated by the command:
#
# raise TypeError('triangle sides must be positive numbers')
#
# If the given values ​​a, b, c cannot form a triangle (condition: each side must be less than
# the sum of the other two), then throw an exception with the command:
#
# raise ValueError('the specified side lengths cannot form a triangle')
#
# Then, based on the following data set:
#
# input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7 , 4, 6)]
#
# it is necessary to generate objects of class Triangle, but only if no exceptions were thrown.
# Present all created objects as a list with the name lst_tr.


class Triangle:
    def __init__(self, a, b, c):
        if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
            raise TypeError("triangle sides must be positive numbers")
        if a <= 0 or b <= 0 or c <= 0:
            raise TypeError("triangle sides must be positive numbers")
        if a > b + c or b > a + c or c > a + b:
            raise ValueError("The given side lengths cannot form a triangle.")
        self._a = a
        self._b = b
        self._c = c


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
lst_tr = []
for data in input_data:
    try:
        triangle = Triangle(*data)
    except(TypeError, ValueError):
        continue
    lst_tr.append(triangle)
for triangle_in in lst_tr:
    print(triangle_in.__dict__)
