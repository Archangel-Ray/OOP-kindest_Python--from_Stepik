# Declare in the program the class Point, the objects of which are to be created by the commands:
#
# pt = Point()
# pt = Point(x, y)
#
# where x, y are arbitrary numbers (point coordinates).
#
# In each object of class Point, local attributes _x, _y must be formed with the corresponding values.
# If no arguments are specified (first command), then _x = 0, _y = 0.
#
# Further, the program enters two values ​​in one line separated by a space.
# Values ​​can be numbers, words, boolean values ​​(True/False).
# You need to read these values ​​from the input stream.
# If both values ​​are numbers, then form the pt object with the command:
#
# pt = Point(x, y)
#
# If at least one of the values ​​is not numeric, then form the pt object with the command:
#
# pt = Point()
#
# Implement this functionality using try/except blocks.
# And in the finally block, display a message in the format (without quotes):
#
# 'Point: x = x value, y = y value'


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


a, b = input().split()
try:
    pt = Point(int(a), int(b))
except:
    pt = Point()
finally:
    print(f"Point: x = {pt.x}, y = {pt.y}")
