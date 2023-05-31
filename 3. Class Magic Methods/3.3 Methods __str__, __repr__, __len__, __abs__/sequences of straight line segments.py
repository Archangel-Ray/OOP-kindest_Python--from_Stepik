# Declare a class PolyLine (polyline) to represent a line from a sequence of straight line segments.
# Objects of this class must be created with the command:
#
# poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
#
# Here start_coord - polyline start coordinate (tuple of two numbers x, y); coord_2, coord_3, ... - subsequent coordinates of points on the plane (represented by tuples) connected by straight lines.
#
# For example:
#
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
#
# The following methods must be declared in the PolyLine class:
#
# add_coord(x, y) - adding a new coordinate (to the end);
# remove_coord(indx) - remove coordinate by index (serial number, starts from zero);
# get_coords() - getting a list of coordinates (as a list of tuples).


class PolyLine:
    def __init__(self, *args):
        self.list_args = list(args)

    def add_coord(self, x, y):
        self.list_args.append((x, y))

    def remove_coord(self, indx):
        if len(self.list_args) > indx:
            self.list_args.pop(indx)

    def get_coords(self):
        return self.list_args


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(5, 10)
poly.remove_coord(4)
poly.remove_coord(4)
poly.add_coord(5, 10)
poly.add_coord(10, 5)
poly.remove_coord(3)
print(poly.get_coords())
