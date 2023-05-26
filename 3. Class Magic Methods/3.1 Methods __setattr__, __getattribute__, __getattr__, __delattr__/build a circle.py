# Declare the class Circle, the objects of which should be created by the command:
#
# circle = Circle(x, y, radius) # x, y - coordinates of the center of the circle; radius - the radius of the circle
#
# Local private attributes must be formed in each object of the Circle class:
#
# __x, __y - coordinates of the center of the circle (real or integer numbers);
# __radius - radius of the circle (real or positive integer).
#
# To access these private attributes in the Circle class, you must declare property objects (property):
#
# x, y - to change and access the values ​​__x, __y, respectively;
# radius - to change and access the __radius value.
#
# When changing the values ​​of private attributes through property objects, you need to check that the assigned values ​​
# are numbers (integer or real). Additionally, check for the radius that the number must be positive
# (strictly greater than zero). All these checks must be done through magical methods. In case of incorrect
# numerical values ​​passed, the previous values ​​should not change (no exceptions need to be generated).
#
# If the assigned value is not numeric, then throw an exception with the command:
#
# raise TypeError('Invalid type of data being assigned.')
#
# When accessing a non-existent attribute of objects of the Circle class, return the boolean value False.
#
# An example of using the class (you do not need to write these lines in the program):
#
# circle = Circle(10.5, 7, 22)
# circle.radius = -10 # the previous value should not change, because negative radius is not allowed
# x, y = circle.x, circle.y
# res = circle.name # False, because name attribute does not exist


class Circle:
    types_dict = {"x": (int, float), "y": (int, float), "radius": (int, float)}

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if key in self.types_dict and type(value) not in self.types_dict[key]:
            raise TypeError('Invalid type of data being assigned.')
        if key == "radius" and value <= 0:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


circle_1 = Circle(10.5, 7, 22)
# circle_2 = Circle('10.5', 7, 22)
# circle_3 = Circle(10.5, 7, -22)
circle_1.radius = -10  # the previous value should not change, because negative radius is not allowed
x, y = circle_1.x, circle_1.y
res = circle_1.name  # False, because name attribute does not exist
print(circle_1.__dict__)
