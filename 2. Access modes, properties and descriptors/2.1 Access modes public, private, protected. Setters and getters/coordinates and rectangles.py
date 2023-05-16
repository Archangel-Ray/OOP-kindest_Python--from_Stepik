# Declare two classes Point and Rectangle in the program. Objects of the first class must be created with the command:
#
# pt = Point(x, y)
#
# where x, y - coordinates of a point on the plane (integers or real numbers). In this case, the following local
# properties should be formed in objects of the Point class:
#
# __x, __y - point coordinates on the plane.
#
# and one getter:
#
# get_coords() - return tuple of current coordinates __x, __y
#
# Objects of the second class Rectangle (rectangle) must be created by the commands:
#
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
#
# or
#
# r2 = Rectangle(x1, y1, x2, y2)
#
# Here the first coordinate (x1, y1) is the top left corner and the second coordinate (x2, y2) is the bottom right.
# At the same time, the following local properties should be formed in objects of the Rectangle class
# (regardless of how they were created):
#
# __sp - object of class Point with coordinates x1, y1 (upper left corner);
# __ep - object of class Point with coordinates x2, y2 (lower right corner).
#
# Also, the following methods must be implemented for the Rectangle class:
#
# set_coords(self, sp, ep) - change the current coordinates, where sp, ep are objects of the Point class;
# get_coords(self) - return a tuple of objects of class Point with the current coordinates of the rectangle
# (references to local properties __sp and __ep);
# draw(self) - display in the console the message: 'Rectangle with coordinates: (x1, y1) (x2, y2)'.
# Here x1, y1, x2, y2 are the corresponding numerical values ​​of the coordinates.
#
# Create a rect object of class Rectangle with coordinates (0, 0), (20, 34).


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None

        if type(a) == Point and type(b) == Point:
            self.__sp = a
            self.__ep = b
        else:
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f"Rectangle with coordinates: {self.__sp.get_coords()}, {self.__ep.get_coords()}")


pt1 = Point(1, 2)
pt2 = Point(3, 4)
print(pt1.get_coords())
rect = Rectangle(0, 0, 20, 34)
rect.draw()
