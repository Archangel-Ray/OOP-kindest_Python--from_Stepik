# The program declares the Point class:
#
# classPoint:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y
#
# And an object of this class is created:
#
# pt = Point(1, 2)
#
# Next, you need to access the z attribute of the pt object and, if such an attribute exists,
# print its value to the screen. Otherwise output the string (without quotes):
#
# 'Attribute named z does not exist'
#
# The check should be implemented using try/except blocks.
#
# Hint: Accessing an attribute that doesn't exist throws an AttributeError exception.


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


pt = Point(1, 2)
try:
    pt.z
except AttributeError:
    print("Attribute named z does not exist")
