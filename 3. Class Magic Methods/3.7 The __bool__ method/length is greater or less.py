# Declare a Line class whose objects are created by the command:
#
# line = Line(x1, y1, x2, y2)
#
# where x1, y1, x2, y2 are the coordinates of the beginning of the line (x1, y1) and the coordinates
# of the end of the line (x2, y2). Can be arbitrary numbers. Corresponding local attributes with names x1, y1, x2, y2
# should be created in objects of class Line.
#
# In the Line class, define the __len__() magic method so that the function:
#
# bool(line)
#
# returned False if the line length is less than 1.


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        len_segment = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        return 0 if len_segment < 1 else int(len_segment)


segment = Line(1, 2, 3, 4)
print(bool(segment))
