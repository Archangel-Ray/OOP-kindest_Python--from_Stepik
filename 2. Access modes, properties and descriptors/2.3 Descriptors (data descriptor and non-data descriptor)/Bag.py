# It is necessary to declare the class Bag (backpack), the objects of which will be created by the command:
#
# bag = Bag(max_weight)
# where max_weight is the maximum total weight of things that the backpack can support (integer).
#
# Each object of this class must have a local private attribute:
#
# __things - list of things in the backpack (list is empty by default).
#
# The Bag class itself must have a property object:
#
# things - to access the local private attribute __things (read only, not write).
#
# The following methods must also be implemented in the Bag class:
#
# add_thing(self, thing) - adding a new item to the backpack (adding is possible if the total weight (max_weight) is not exceeded, otherwise the addition does not occur);
# remove_thing(self, indx) - remove item by index of __things list;
# get_total_weight(self) - Returns the total weight of the items in the backpack.
#
# Each thing is described as an object of the Thing class and created by the command:
#
# t = Thing(name, weight)
# where name is the name of the item (string); weight - the weight of the object (integer or real number).
#
# Local attributes must be formed in each object of the Thing class:
#
# name - item name;
# weight - the weight of the item.
#
# An example of using classes (you do not need to write these lines in the program):
#
# bag = Bag(1000)
# bag.add_thing(Thing('Python book', 100))
# bag.add_thing(Thing('Bowler', 500))
# bag.add_thing(Thing('Matches', 20))
# bag.add_thing(Thing('Paper', 100))
# w = bag.get_total_weight()
# for t in bag.things:
# print(f'{t.name}: {t.weight}')


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        now_weight = self.get_total_weight()
        if now_weight + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(t.weight for t in self.__things)


bag = Bag(1000)
bag.add_thing(Thing("Python book", 100))
bag.add_thing(Thing("Bowler", 500))
bag.add_thing(Thing("Matches", 20))
bag.add_thing(Thing("Paper", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
