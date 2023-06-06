# Declare a class Track (route), whose objects are created by the command:
#
# track = Track(start_x, start_y)
#
# where start_x, start_y - coordinates of the beginning of the route (integer or real numbers).
#
# Each linear segment of the route is defined by the TrackLine class, the objects of which are created by the command:
#
# line = TrackLine(to_x, to_y, max_speed)
#
# where to_x, to_y - coordinates of the next route point (integer or real numbers);
# max_speed - maximum speed in this section (integer).
#
# To form and work with a route, the following methods must be declared in the Track class:
#
# add_track(self, tr) - adding a linear segment of the route (next point);
# get_tracks(self) - getting a tuple of TrackLine class objects.
#
# Also, for objects of the Track class, the following comparison operations must be implemented:
#
# track1 == track2 # routes are equal if their lengths are equal
# track1 != track2 # routes are not equal if their lengths are not equal
# track1 track2 # True if track1 is longer than track2
# track1 track2 # True if track1's path length is less than track2's
#
# And the function:
#
# n = len(track) # returns the integer length of the route (cast to int) for the track object
#
# Create two routes track1 and track2 with coordinates:
#
# 1st route: (0; 0), (2; 4), (5; -4) and max_speed = 100
# 2nd route: (0; 1), (3; 2), (10; 8) and max_speed = 90
#
# Compare them to each other for equality. Save the comparison result in the res_eq variable.


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.route = []

    def add_track(self, tr):
        self.route.append(tr)

    def get_tracks(self):
        return tuple(self.route)

    def __len__(self):
        start_segment_length = ((self.start_x - self.route[0].to_x) ** 2 +
                                (self.start_y - self.route[0].to_y) ** 2) ** 0.5
        return int(start_segment_length + sum(self.__get_length(i) for i in range(1, len(self.route))))

    def __get_length(self, ind):
        return ((self.route[ind-1].to_x - self.route[ind].to_x) ** 2 +
                (self.route[ind-1].to_y - self.route[ind].to_y) ** 2) ** 0.5

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
