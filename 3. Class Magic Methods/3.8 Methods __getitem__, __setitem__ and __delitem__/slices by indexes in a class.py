# Declare in the program a class named RadiusVector (radius vector), whose objects are created by the command:
#
# v = RadiusVector(x1, x2,..., xN)
#
# where x1, x2,..., xN are the coordinates of the radius vector (numbers: integer or real).
#
# Each object of class RadiusVector must have a local attribute:
#
# coords - a list of radius vector coordinates.
#
# To access individual coordinates, implement the following functionality:
#
# coord = v[i] # getting the value of the i-th coordinate (integer, counting from zero)
# coords_1 = v[start:stop] # getting a slice (set) of coordinates as a tuple
# coords_2 = v[start:stop:step] # getting a slice (set) of coordinates as a tuple
# v[i] = value # change i-th coordinate
# v[start:stop] = [val_1, val_2, ...] # changing multiple coordinates at once
# v[start:stop:step] = [val_1, val_2, ...] # changing multiple coordinates at once
#
# An example of using the class (do not write these lines in the program):
#
# v = RadiusVector(1, 1, 1, 1)
# print(v[1]) # 1
# v[:] = 1, 2, 3, 4
# print(v[2]) # 3
# print(v[1:]) # (2, 3, 4)
# v[0] = 10.5
#
# P.S. When passing a slice in the __setitem__() and __getitem__() magic methods, the index parameter becomes an object
# of the slice class. It can be specified directly in square brackets of ordered collections (lists, tuples, etc.).


class RadiusVector:
    def __init__(self, *args):
        self.coords = list(args)

    def __getitem__(self, item):
        return tuple(self.coords[item]) if type(item) == slice else self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
