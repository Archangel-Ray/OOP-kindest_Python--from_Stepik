# Declare the Box3D class to represent a cuboid (bar) whose objects are created by the command:
#
# box = Box3D(width, height, depth)
#
# where width, height, depth - width, height and depth respectively (numbers: integer or real)
#
# Public attributes must be created in each Box3D class object:
#
# width, height, depth - width, height and depth respectively.
#
# The following statements must be executed with objects of the Box3D class:
#
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (corresponding dimensions are added together)
# box = box1 * 2 # Box3D: width=2, height=4, depth=6 (each dimension is multiplied by 2)
# box = 3 * box2 # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (corresponding dimensions are subtracted)
# box = box1 // 2 # Box3D: width=0, height=1, depth=1 (corresponding dimensions are integer divisible by 2)
# box = box2 % 3 # Box3D: width=2, height=1, depth=0
#
# For each arithmetic operation, a new object of the Box3D class should be created with the corresponding
# local attribute values.


class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width + other, self.height + other, self.depth + other)
        if type(other) == Box3D:
            return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __radd__(self, other):
        return Box3D(other + self.width, other + self.height, other + self.depth)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width * other, self.height * other, self.depth * other)
        if type(other) == Box3D:
            return Box3D(self.width * other.width, self.height * other.height, self.depth * other.depth)

    def __rmul__(self, other):
        return Box3D(other * self.width, other * self.height, other * self.depth)

    def __sub__(self, other):
        if type(other) in (int, float):
            return Box3D(self.width - other, self.height - other, self.depth - other)
        if type(other) == Box3D:
            return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __rsub__(self, other):
        return Box3D(other - self.width, other - self.height, other - self.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + 2
box = box1 + box2
box = box1 * 2
box = 3 * box2
box = box2 - box1
box = box1 // 2
box = box2 % 3
print(box.__dict__)
