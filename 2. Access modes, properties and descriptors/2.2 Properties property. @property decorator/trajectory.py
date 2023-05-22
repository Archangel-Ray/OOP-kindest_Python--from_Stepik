# You need to generate a PathLines class to describe routes that consist of line segments. In this case, each linear
# segment is supposed to be specified by a separate LineTo class. Objects of this class will be formed by the command:
#
# line = LineTo(x, y)
#
# where x, y - the next coordinate of the linear section (the beginning of the route from the point 0, 0).
#
# Local attributes must be formed in each object of the LineTo class:
#
# x, y - to store the coordinates of the end of the line (the beginning is determined by the coordinates
# of the previous object).
#
# Objects of the PathLines class must be created with the commands:
#
# p = PathLines()                 # path start from point 0, 0
# p = PathLines(line1, line2, ...) # start path from point 0, 0
#
# where line1, line2, ... are objects of class LineTo.
#
# The PathLines class itself must have the following methods:
#
# get_path() - returns a list of objects of the LineTo class (if there are no objects, then an empty list);
# get_length() - returns the total length of the path (the sum of the lengths of all line segments);
# add_line(self, line) - adding a new line segment (object of the LineTo class) to the end of the route.
#
# Explanation: the total route is the sum of the lengths of all line segments, and the length of each line segment
# is determined as the Euclidean distance using the formula:
#
# L = sqrt((x1-x0)~2 + (y1-y0)~2)
#
# where x0, y0 - previous route point; x1, y1 - current waypoint.
#
# An example of using classes (you do not need to write these lines in the program):
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.path = [LineTo(0, 0), *args]

    def get_path(self):
        return self.path[1:]

    def get_length(self):
        list_args = self.path
        sum_value = 0
        for ind in range(len(list_args)-1):
            x0 = list_args[ind].x
            y0 = list_args[ind].y
            x1 = list_args[ind+1].x
            y1 = list_args[ind+1].y
            sum_value += ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
        return sum_value

    def add_line(self, line):
        self.path.append(line)


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
print(*[(arg.x, arg.y) for arg in p.get_path()], sep='\n')

en = PathLines(LineTo(1, 2))
print(en.get_length())  # 2.23606797749979
en.add_line(LineTo(10, 20))
en.add_line(LineTo(5, 10))
print(en.get_length())  # 28.191631669843197
m = en.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []
