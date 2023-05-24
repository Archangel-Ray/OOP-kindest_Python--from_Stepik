# You need to write a program to present and manage the TV broadcast schedule. To do this, you need to declare
# the TVProgram class, the objects of which are created by the command:
#
# pr = TVProgram(channel name)
#
# where channel name is a string with the name of the TV channel.
#
# Each object of the TVProgram class must have a local attribute:
#
# items - list of TV programs (initially the list is empty).
#
# The following methods must be implemented in the TVProgram class itself:
#
# add_telecast(self, tl) - adding a new TV show to the items list;
# remove_telecast(self, indx) - remove a telecast by its sequence number (attribute __id, see below).
#
# Each telecast must be described by the Telecast class, whose objects are created by the command:
#
# tl = Telecast(number, name, duration)
#
# where serial number is the number of the TV show in the broadcasting grid (from 1 onwards); name - the name
# of the TV show; duration - TV transmission time (in seconds - an integer).
#
# Accordingly, in each object of the Telecast class, local private attributes should be formed:
#
# __id - sequence number (integer);
# __name - TV show name (string);
# __duration - TV show duration in seconds (integer).
#
# To work with these private attributes, the corresponding property objects must be declared in the Telecast class:
#
# uid - for writing and reading from the local __id attribute;
# name - for writing and reading from the local attribute __name;
# duration - for writing to and reading from the local __duration attribute.
#
# An example of using classes (you do not need to write these lines in the program):
#
# pr = TVProgram('First channel')
# pr.add_telecast(Telecast(1, 'Good morning', 10000))
# pr.add_telecast(Telecast(2, 'News', 2000))
# pr.add_telecast(Telecast(3, 'Interview with Balakirev', 20))
# for t in pr.items:
# print(f'{t.name}: {t.duration}')


class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        tl_del = tuple(filter(lambda x: x.uid == indx, self.items))
        for tl in tl_del:
            self.items.remove(tl)


pr = TVProgram("First channel")
pr.add_telecast(Telecast(1, "Good morning", 10000))
pr.add_telecast(Telecast(2, "News", 2000))
pr.add_telecast(Telecast(3, "Interview with Balakirev", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
