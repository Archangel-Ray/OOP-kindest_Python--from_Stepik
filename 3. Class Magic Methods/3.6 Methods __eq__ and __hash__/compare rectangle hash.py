# Declare in the program a class named Rect (rectangle), whose objects are created by the command:
#
# rect = Rect(x, y, width, height)
#
# where x, y - coordinate of the upper left corner (numbers: integer or real); width, height - width and height
# of the rectangle (numbers: integer or real).
#
# In this class, define a magic method so that the hashes of Rect class objects with equal width, height are equal.
# For example:
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)   # h1 == h2


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == self.height and other.width == other.height

    def __hash__(self):
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)
print(h1 == h2)


class Index:
    START_INDEX = 0

    def __init__(self):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1

    def __hash__(self):
        return hash(str(self.id))


id1 = Index()
id2 = Index()
d = {id1: id1, id2: id2}
print(d)
