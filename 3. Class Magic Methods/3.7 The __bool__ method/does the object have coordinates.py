# Declare the class Ellipse, whose objects are created by the commands:
#
# el1 = Ellipse() # without creating local attributes x1, y1, x2, y2
# el2 = Ellipse(x1, y1, x2, y2)
#
# where x1, y1 - coordinates (numbers) of the upper left corner; x2, y2 - coordinates (numbers) of the lower right
# corner. The first command creates an object of class Ellipse without local attributes x1, y1, x2, y2. The second
# command creates an object with local attributes x1, y1, x2, y2 and the corresponding values ​​passed in.
#
# In the Ellipse class, declare a __bool__() magic method that would return True if all local
# attributes x1, y1, x2, y2 exist and False otherwise.
#
# Also in the Ellipse class, you need to implement the method:
#
# get_coords() - to get a tuple of the object's current coordinates.
#
# If there are no coordinates (no local attributes x1, y1, x2, y2), then the get_coords() method must throw
# an exception with the command:
#
# raise AttributeError('no coordinates to retrieve')
#
# Create a list in the program called lst_geom containing four objects of class Ellipse.
# Two objects must be created by the command
#
# Ellipse()
#
# and two more - with the command:
#
# Ellipse(x1, y1, x2, y2)
#
# Loop through the list and call the get_coords() method only for objects that have x1, y1, x2, y2 coordinates.
# (Remember that the __bool__() magic method was defined for this).


class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return True if len(self.__dict__) == 4 else False

    def get_coords(self):
        if self.__bool__():
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError("no coordinates to retrieve")


lst_geom = [Ellipse(), Ellipse(2, 2, 3, 3), Ellipse(), Ellipse(5, 5, 5, 5)]
for ellipse in lst_geom:
    if ellipse:
        ellipse.get_coords()

print(lst_geom)
