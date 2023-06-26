# Declare a base class named ItemAttrs that allows you to access the local attributes of child class objects by index.
# To do this, you need to override the following methods in the ItemAttrs class:
#
# __getitem__() - to get attribute value by index;
# __setitem__() - to change the value of an attribute by index.
#
# Declare a child class Point to represent the coordinate of a point on the plane.
# Objects of this class must be created with the command:
#
# pt = Point(x, y)
#
# where x, y are integer or real numbers.
#
# An example of using classes (do not write these lines in the program):
#
# pt = Point(1, 2.5)
# x = pt[0] # 1
# y = pt[1] # 2.5
# pt[0] = 10


class ItemAttrs:
    def __init__(self, *args):
        self.args = list(args)

    def __getitem__(self, item):
        return self.args[item]

    def __setitem__(self, key, value):
        self.args[key] = value


class Point(ItemAttrs):
    pass


pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
pt[0] = 10
