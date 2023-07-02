# You are tasked with developing a class to represent routes in a navigator.
# This requires declaring a class named Track, whose objects can be created by commands:
#
# tr = Track(start_x, start_y)
# tr = Track(pt1, pt2, ..., ptN)
#
# where start_x, start_y - starting coordinate of the route (arbitrary numbers);
# pt1, pt2, ..., ptN - a set of an arbitrary number of points (coordinates)
# of the route (objects of the PointTrack class).
#
# When passing arguments (start_x, start_y), the coordinate must be represented by the first object
# of the PointTrack class. The sets of all points (PointTrack objects)
# must be stored in a local private attribute of the Track class object:
#
# __points - a list of points (coordinates) of the route.
#
# Further, each point (coordinate) must be defined by the PointTrack class, whose objects are created by the command:
#
# pt = PointTrack(x, y)
#
# where x, y are numbers (integer or real).
# If another data type is passed, then an exception must be thrown with the command:
#
# raise TypeError('coordinates must be numbers')
#
# In the PointTrack class, override the __str__ magic method to return information about the class object as a string:
#
# "PointTrack: <x>, <y>"
#
# For example:
#
# pt = PointTrack(1, 2)
# print(pt) # PointTrack: 1, 2
#
# The Track class itself should have a property named:
#
# points - to get a tuple of route points.
#
# Also, the Track class should have methods:
#
# def add_back(self, pt) - adding a new point to the end of the route (pt is an object of the PointTrack class);
# def add_front(self, pt) - adding a new point to the beginning of the route (pt is an object of the PointTrack class);
# def pop_back(self) - remove the last point from the route;
# def pop_front(self) - remove the first point from the route.
#
# An example of using classes (you do not need to write these lines in the program):
#
# tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
# tr.add_back(PointTrack(1.4, 0))
# tr.pop_front()
# for pt in tr points:
#     print(pt)


class PointTrack:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check(self, value):
        if type(value) not in (int, float):
            raise TypeError("coordinates must be numbers")
        return value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.check(value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.check(value)
        self.__y = value

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


class Track:
    def __init__(self, *args):
        self.__points = []
        if type(args[0]) != PointTrack:
            if len(args) == 2:
                self.__points.append(PointTrack(args[0], args[1]))
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points = self.__points[1:]


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
