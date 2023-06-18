# Declare the Bag class in the program, the objects of which are created by the command:
#
# bag = Bag(max_weight)
#
# where max_weight is the maximum total weight of items that can be put in the bag.
#
# Each item is described by the Thing class and created by the command:
#
# t = Thing(name, weight)
#
# where name - item name (string); weight - item weight (real or integer value). Objects of the Thing class
# should automatically generate local properties with the same names: name and weight.
#
# The Bag class must implement the following method:
#
# add_thing(thing) - Add a new Thing object to the bag.
#
# Adding is performed only if the total weight of things does not exceed the max_weight parameter.
# Otherwise, an exception is thrown:
#
# raise ValueError('total item weight exceeded')
#
# Also, the following commands must be executed with objects of the Bag class:
#
# t = bag[indx] # getting a Thing object at index indx (in order of adding things, starting from 0)
# bag[indx] = t # replace the old thing with a new one t located at index indx
# del bag[indx] # remove item from bag located at indx index
#
# If the index in these commands is incorrect, then an exception should be thrown:
#
# raise IndexError('invalid index')
#
# An example of using classes (do not write these lines in the program):
#
# bag = Bag(1000)
# bag.add_thing(Thing('book', 100))
# bag.add_thing(Thing('socks', 200))
# bag.add_thing(Thing('shirt', 500))
# bag.add_thing(Thing('scissors', 300)) # throws a ValueError exception
# print(bag[2].name) # shirt
# bag[1] = Thing('handkerchief', 100)
# print(bag[1].name) # handkerchief
# del bag[0]
# print(bag[0].name) # handkerchief
# t = bag[4] # an IndexError is thrown


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__weight = 0
        self.__things = []

    def __check_weight(self, new_thing, old_thing=None):
        new_weight = self.__weight + new_thing.weight if old_thing is None \
            else self.__weight + new_thing.weight - old_thing.weight
        if new_weight > self.max_weight:
            raise ValueError('total weight of items exceeded')

    def __check_index(self, indx):
        if not (0 <= indx < len(self.__things)):
            raise IndexError('invalid index')

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.__things.append(thing)
        self.__weight += thing.weight

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__things[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__check_weight(value, self.__things[key])
        self.__weight += (value.weight - self.__things[key].weight)
        self.__things[key] = value

    def __delitem__(self, key):
        self.__check_index(key)
        self.__weight -= self.__things.pop(key).weight


bag = Bag(1000)
bag.add_thing(Thing('book', 100))
bag.add_thing(Thing('socks', 200))
bag.add_thing(Thing('shirt', 500))
# bag.add_thing(Thing('scissors', 300))
print(bag[2].name)
bag[1] = Thing('shawl', 100)
print(bag[1].name)
del bag[0]
print(bag[0].name)
# t = bag[4]
