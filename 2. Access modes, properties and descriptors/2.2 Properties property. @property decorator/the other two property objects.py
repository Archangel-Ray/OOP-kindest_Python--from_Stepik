# Declare a RadiusVector2D class whose objects are to be created with the commands:
#
# v1 = RadiusVector2D()       # radius vector with coordinates (0; 0)
# v2 = RadiusVector2D(1)      # radius vector with coordinates (1; 0)
# v3 = RadiusVector2D(1, 2)   # radius vector with coordinates (1; 2)
# In each object of the class RadiusVector2D, local private attributes must be formed:
#
# __x, __y - coordinates of the end of the vector (initially, the values ​​are 0 if no other is passed).
#
# In the RadiusVector2D class, you need to declare two property objects:
#
# x - to change and read the local attribute __x;
# y - to change and read the local attribute __y.
#
# When initializing and changing local attributes, it is necessary to check the correctness of the passed values:
#
# - the value must be a number (integer or real) in the range [MIN_COORD; MAX_COORD].
#
# If the check fails, then the coordinates do not change (recall that they are initially equal to 0 during
# initialization). The values ​​MIN_COORD = -100, MAX_COORD = 1024 are set as public attributes
# of the RadiusVector2D class.
#
# You also need to declare a static method in the RadiusVector2D class:
#
# norm2(vector) - to calculate the quadratic norm of vector - the passed object of class RadiusVector2D
# (quadratic norm of the vector: x*x + y*y).


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.coord_check(x):
            self.__x = x
        if self.coord_check(y):
            self.__y = y

    @classmethod
    def coord_check(cls, coord):
        if type(coord) in (int, float):
            if cls.MIN_COORD < coord < cls.MAX_COORD:
                return True
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.coord_check(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.coord_check(y):
            self.__y = y

    @staticmethod
    def norm2(vector):
        x = vector.x
        y = vector.y
        return x * x + y * y


coord_1 = RadiusVector2D()
coord_2 = RadiusVector2D(1)
coord_3 = RadiusVector2D(2, 3)
r5 = RadiusVector2D(-102, 2000)
coord_1.x = 5
coord_1.y = 7.5
coord_2.y = 10.46
coord_3.x = -1000
coord_3.y = "12.654"
norm_2 = RadiusVector2D.norm2(coord_1)
print(coord_1.__dict__, coord_2.__dict__, coord_3.__dict__, r5.__dict__, norm_2, sep="\n")
