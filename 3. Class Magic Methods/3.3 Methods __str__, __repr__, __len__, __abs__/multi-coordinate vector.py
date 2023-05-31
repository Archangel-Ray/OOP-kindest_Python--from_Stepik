# Declare a class named RadiusVector to describe and work with an n-dimensional vector (which has n coordinates).
# Objects of this class must be created with the commands:
#
# create a 5-dimensional radius vector with zero coordinate values ​​(argument is an integer greater than 1)
# vector = RadiusVector(5) # coordinates: 0, 0, 0, 0, 0
#
# create a 4-dimensional radius vector with coordinates: 1, -5, 3.4, 10 (coordinates are any integer or real numbers)
# vector = RadiusVector(1, -5, 3.4, 10)
#
# That is, when passing a single value, it is interpreted as the dimension of the zero radius vector.
# If more than one numeric argument is passed, then they are interpreted as the coordinates of the radius vector.
#
# The RadiusVector class must contain methods:
#
# set_coords(coord_1, coord_2, ..., coord_N) - to change the coordinates of the radius vector;
# get_coords() - to get the current coordinates of the radius vector (as a tuple).
#
# Also with objects of class RadiusVector the following functions should be supported:
#
# len(vector) - returns the number of coordinates of the radius vector (its dimension);
# abs(vector) - returns the length of the radius vector
# (calculated as: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N)
# - the square root of the sum of squared coordinates).
#
# An example of using the RadiusVector class (these lines do not need to be written in the program):
#
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11) # should not cause an error, the last two coordinates are ignored
# vector3D.set_coords(1, 2) # Shouldn't be an error, only the first two coordinates change
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)


class RadiusVector:
    def __init__(self, arg, *args):
        if not args:
            self.__coords = [0] * arg
        else:
            self.__coords = [arg] + list(args)

    def set_coords(self, *args):
        if len(args) >= len(self.__coords):
            for ind in range(len(self.__coords)):
                self.__coords[ind] = args[ind]
        else:
            for ind in range(len(args)):
                self.__coords[ind] = args[ind]

    def get_coords(self):
        return tuple(self.__coords)

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        sum_of_squares = 0
        for value in self.__coords:
            sum_of_squares += value * value
        return sum_of_squares ** 0.5


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)
vector3D.set_coords(1, 2)
res_len = len(vector3D)
res_abs = abs(vector3D)
print(res_abs, res_len, [a, b, c], sep="\n")
