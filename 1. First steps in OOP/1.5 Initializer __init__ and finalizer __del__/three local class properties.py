# Declare the Point class so that objects of this class can be created with commands:
#
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
# Here, the first two values ​​are the coordinates of the point on the plane (local properties x, y), and the third
# optional argument is the color of the point (local property color). If no color is specified, it defaults to black.
#
# Create a thousand of these objects at coordinates (1, 1), (3, 3), (5, 5), ... that is, incremented by two for each
# new point. Each object should be placed in the points list (in order). For the second object in the points list,
# set the color to 'yellow'.
#
# P.S. You don't need to display anything on the screen.


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for index in range(1, 2001, 2):
    if index == 3:
        point = Point(index, index, 'yellow')
        points.append(point)
    else:
        point = Point(index, index)
        points.append(point)

for i in points:
    print(i.__dict__)
print(len(points))
