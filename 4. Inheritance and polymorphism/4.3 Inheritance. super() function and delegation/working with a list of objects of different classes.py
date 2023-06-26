# You are instructed to organize the presentation of objects for sale in real estate agencies.
# To do this, the program needs to declare the base class SellItem, whose objects are created by the command:
#
# item = SellItem(name, price)
#
# where name - the name of the object of sale (string); price - sale price (number: integer or real).
#
# Each specific object type is described by the following classes, inherited from the base SellItem:
#
# House - at home;
# Flat - apartments;
# Land - land plots.
#
# Objects of these classes are created by the commands:
#
# house = House(name, price, material, square)
# flat = Flat(name, price, size, rooms)
# land = Land(name, price, square)
#
# In each object of these classes, the corresponding local attributes must be formed: name, price, etc.
#
# The name and price attributes must be generated in the base class initializer.
#
# Next, declare another class named Agency, whose objects are created by the command:
#
# ag = agency(name)
#
# where name is the name of the agency (string). Declare the following methods in the Agency class:
#
# add_object(obj) - adding a new property for sale (one of the class objects: House, Flat, Land);
# remove_object(obj) - remove object obj from the list of objects for sale;
# get_objects() - returns a list of all objects for sale.
#
# An example of using classes (do not write these lines in the program):
#
# ag = Agency('Horns and hooves')
# ag.add_object(Flat('apartment, 3k', 10000000, 121.5, 3))
# ag.add_object(Flat('apartment, 2k', 8000000, 74.5, 2))
# ag.add_object(Flat('apartment, 1k', 4000000, 54, 1))
# ag.add_object(House('house, brick', price=35000000, material='brick', square=186.5))
# ag.add_object(Land('building land', 3000000, 6.74))
# for obj in ag.get_objects():
#     print(obj.name)
#
# lst_houses = [x for x in ag.get_objects() if isinstance(x, House)] # extract list of houses


class SellItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        self.name = name
        self.list_objects = []

    def add_object(self, obj):
        self.list_objects.append(obj)

    def remove_object(self, obj):
        if obj in self.list_objects:
            self.list_objects.remove(obj)

    def get_objects(self):
        return self.list_objects


ag = Agency("Horns and hooves")
ag.add_object(Flat("apartment, 3r", 10000000, 121.5, 3))
ag.add_object(Flat("apartment, 2r", 8000000, 74.5, 2))
ag.add_object(Flat("apartment, 1r", 4000000, 54, 1))
ag.add_object(House("house, brick", price=35000000, material="brick", square=186.5))
ag.add_object(Land("building plot", 3000000, 6.74))
for obj in ag.get_objects():
    print(obj.name)

lst_houses = [x for x in ag.get_objects() if isinstance(x, House)]
print(lst_houses)
