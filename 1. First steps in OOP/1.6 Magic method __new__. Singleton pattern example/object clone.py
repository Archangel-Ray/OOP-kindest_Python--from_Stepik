# Declare a Point class to represent points on a plane.
# It is supposed to create objects of this class with the command:
#
# pt = Point(x, y)
#
# Here x, y are the numerical coordinates of a point on the plane (numbers), that is, in each object of this class,
# local properties x, y are created that store the specific coordinates of the point.
#
# It is necessary to implement the clone(self) method in the Point class, which would create a new object
# of the Point class as a copy of the current object with local attributes x, y and corresponding values.
#
# Create a pt object of the Point class and another pt_clone object in the program by calling the clone method.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(1, 2)
pt_clone = pt.clone()
print(pt.__dict__, pt_clone.__dict__, sep='\n')
