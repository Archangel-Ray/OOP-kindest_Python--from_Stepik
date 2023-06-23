# Declare the Vector class in the program, the objects of which are created by the command:
#
# v = Vector(x1, x2, ..., xN)
#
# where x1, x2, ..., xN - coordinates of the radius vector (numbers: integer or real).
#
# The following commands should be executed with objects of this class:
#
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2 # a new vector is formed (an object of the Vector class) with the corresponding coordinates
# v = v1 - v2 # a new vector is formed (an object of the Vector class) with the corresponding coordinates
#
# If the dimensions of the vectors v1 and v2 do not match, then throw an exception:
#
# raise TypeError('vector dimensions do not match')
#
# In the Vector class itself, declare a method named get_coords that returns
# a tuple of the vector's current coordinates.
#
# Based on the Vector class, declare a VectorInt child class to work with integer coordinates:
#
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # error: an exception is thrown raise ValueError('coordinates must be integers')
#
# During addition and subtraction operations with an object of the VectorInt class:
#
# v = v1 + v2 # v1 is an object of class VectorInt
# v = v1 - v2 # v1 - object of class VectorInt
#
# the object v must be formed as an object of class Vector if at least one coordinate is real.
# Otherwise, v must be an object of the VectorInt class.


class Vector:
    _allowed_types = (int, float)

    def __init__(self, *coords):
        self.__check_coords(coords)
        self._coords = coords

    def __check_coords(self, coords):
        if not all(type(x) in self._allowed_types for x in coords):
            raise ValueError("wrong type of coordinates")

    def get_coords(self):
        return tuple(self._coords)

    @staticmethod
    def __is_vector(obj):
        if not isinstance(obj, Vector):
            raise TypeError("operant must be an object of class Vector")

    def __check_vector_dims(self, other):
        if len(self._coords) != len(other.get_coords()):
            raise TypeError('the dimensions of the vectors do not match')

    def __make_vector(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)

    def __add__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)

        coords = tuple(a + b for a, b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)

    def __sub__(self, other):
        self.__is_vector(other)
        self.__check_vector_dims(other)

        coords = tuple(a - b for a, b in zip(self._coords, other.get_coords()))
        return self.__make_vector(coords)


class VectorInt(Vector):
    _allowed_types = (int, )


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2
v = v1 - v2
v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4)
