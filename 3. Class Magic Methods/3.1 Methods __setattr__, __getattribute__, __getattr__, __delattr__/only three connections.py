# Declare the class GeyserClassic - a filter for water purification. This class should have three filter slots.
# Each slot is strictly for its own filter class:
#
# Mechanical - for cleaning from large mechanical particles;
# Aragon - for subsequent water treatment;
# Calcium - for water treatment in the third stage.
#
# Filter class objects must be created with the commands:
#
# filter_1 = Mechanical(install date)
# filter_2 = Aragon(set date)
# filter_3 = Calcium(install date)
#
# All objects of these classes must have a local attribute:
#
# date - date of filters installation (for simplicity - a positive real number).
#
# You also need to prohibit changing this attribute after creating objects of these classes (read-only).
# If a new value is assigned, do not change the previous value. Do not generate any errors.
#
# Objects of the GeyserClassic class must be created with the command:
#
# g = GeyserClassic()
#
# And the class itself has an attribute:
#
# MAX_DATE_FILTER = 100 - maximum filter time (any)
#
# and the following methods:
#
# add_filter(self, slot_num, filter) - adding the filter filter to the specified slot_num (slot number: 1, 2 and 3)
# if it (slot) is empty (no filter). You should also check here that only Mechanical objects can be installed
# in the first slot, objects of the Aragon class in the second slot, and objects of the Calcium class in the third slot.
# Otherwise, the slot must remain empty.
#
# remove_filter(self, slot_num) - remove the filter from the specified slot (slot_num: 1, 2, and 3);
#
# get_filters(self) - returns a tuple from a set of three filters in the order they are installed
# (in ascending slot numbers);
#
# water_on(self) - turn on water: returns True if water is flowing and False otherwise.
#
# The water_on() method must return True if the following conditions are met:
#
# - all three filters are installed in the slots;
# - all filters work within lifetime (value (time.time() - date) must be within [0; MAX_DATE_FILTER])
#
# An example of using classes (you do not need to write these lines in the program):
#
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
# w = my_water.water_on() # False
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on() # True
# f1, f2, f3 = my_water.get_filters() # f1, f2, f3 - references to the corresponding filter class objects
# my_water.add_filter(3, Calcium(time.time())) # re-adding to an occupied slot is not possible
# my_water.add_filter(2, Calcium(time.time())) # adding to 'foreign' slot is also impossible
import time


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date


class Calcium:
    def __init__(self, date):
        self.date = date


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filter_class = ("Mechanical", "Aragon", "Calcium")
    def __init__(self):

        self.filters = {(1, self.filter_class[0]): None,
                        (2, self.filter_class[1]): None,
                        (3, self.filter_class[2]): None,}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filter

    def remove_filter(self, slot_num):
        if slot_num in (1, 2, 3):
            key = (slot_num, self.filter_class[slot_num - 1])
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        end = time.time()
        for filt in self.filters.values():
            if filt is None:
                return False
            start = filt.date
            if end - start > self.MAX_DATE_FILTER:
                return False
        return True


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
print(my_water.water_on())  # False
my_water.add_filter(3, Calcium(time.time()))
print(my_water.water_on())  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - references to the corresponding filter class objects
my_water.add_filter(3, Calcium(time.time()))  # re-adding to an occupied slot is not possible
my_water.add_filter(2, Calcium(time.time()))  # adding to a "foreign" slot is also impossible
my_water.remove_filter(3)
my_water.remove_filter(2)
print(my_water.get_filters())
my_water.add_filter(2, f2)
my_water.add_filter(3, f1)
my_water.add_filter(3, f3)
print(my_water.water_on())
