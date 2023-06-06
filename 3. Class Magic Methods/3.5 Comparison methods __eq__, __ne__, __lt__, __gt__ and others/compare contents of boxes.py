# Declare in the program a class named Box (box), whose objects are to be created by the command:
#
# box = Box()
#
# And the class itself has the following methods:
#
# add_thing(self, obj) - adding an object obj (an object of another Thing class) to the box;
# get_things(self) - get a list of box objects.
#
# To describe items, you need to declare another Thing class. Objects of this class must be created with the command:
#
# obj = Thing(name, mass)
#
# where name - item name (string); mass - object mass (number: integer or real).
# Thing class objects must support comparison operators:
#
# obj1 == obj2
# obj1 != obj2
#
# Items are considered equal if they have the same name (case insensitive) and mass.
#
# Also, objects of the Box class must support similar comparison operators:
#
# box1 == box2
# box1 != box2
#
# Boxes are considered equal if their contents are the same (for each Thing class object of one box, exactly one equal
# object from the second box can be found).
#
# An example of using classes:
#
# b1 = Box()
# b2 = Box()
#
# b1.add_thing(Thing('chalk', 100))
# b1.add_thing(Thing('rag', 200))
# b1.add_thing(Thing('board', 2000))
#
# b2.add_thing(Thing('rag', 200))
# b2.add_thing(Thing('chalk', 100))
# b2.add_thing(Thing('board', 2000))
#
# res = b1 == b2 # True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


class Box:
    def __init__(self):
        self.list_object = []

    def get_things(self):
        return self.list_object

    def add_thing(self, obj):
        self.list_object.append(obj)

    def __eq__(self, other):
        save_list_self = dict()
        save_list_other = dict()
        for obj in self.list_object:
            save_list_self[obj.name.lower()] = obj.mass
        for obj in other.list_object:
            save_list_other[obj.name.lower()] = obj.mass
        return save_list_self == save_list_other


b1 = Box()
b2 = Box()

b1.add_thing(Thing('chalk', 100))
b1.add_thing(Thing('rag', 200))
b1.add_thing(Thing('board', 2000))

b2.add_thing(Thing('Rag', 200))
b2.add_thing(Thing('Chalk', 100))
b2.add_thing(Thing('Board', 2000))

check = b1.get_things()[0] != b2.get_things()[0]
res = b1 == b2
print(res)
