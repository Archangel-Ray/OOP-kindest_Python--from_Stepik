# Declare a Line class to describe a line on a plane whose objects are supposed to be created by the command:
#
# line = Line(x1, y1, x2, y2)
# In this case, the following private local properties should be created in the line object:
#
# __x1, __y1 - initial coordinate;
# __x2, __y2 - end coordinate.
#
# The following setters and getters must be implemented in the Line class itself:
#
# set_coords(self, x1, y1, x2, y2) - to change line coordinates;
# get_coords(self) - to get a tuple of the line's current coordinates.
#
# And also the method:
#
# draw(self) - to display in the console a list of the current coordinates of the line
# (in one line separated by a space).


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)


line = Line(1, 2, 3, 4)
line.draw()
line.set_coords(6, 7, 8, 9)
print(line.get_coords())
line.draw()
