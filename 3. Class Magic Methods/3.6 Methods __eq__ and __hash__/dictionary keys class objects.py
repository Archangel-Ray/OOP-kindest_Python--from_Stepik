# Declare a class named ShopItem (product) whose objects are created by the command:
#
# item = ShopItem(name, weight, price)
#
# where name - product name (string); weight - product weight (number: integer or real);
# price - item price (number: integer or real).
#
# Define magic methods in this class:
#
# __hash__() - so that products with the same name (case insensitive), weight and price have equal hashes;
# __eq__() - so that objects with the same hashes are equal.
#
# Then, read the lines from the input stream with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# The lines have the following format:
#
# product name 1: weight_1 price_1
# ...
# product name N: weight_N price_N
#
# For example:
#
# System block: 1500 75890.56
# Monitor Samsung: 2000 34000
# Keyboard: 200.44545
# Monitor Samsung: 2000 34000
#
# As you can see, the items in this list may overlap.
#
# It is necessary for all these lines to form the corresponding objects of the ShopItem class and add them
# to the dictionary with the name shop_items. The keys of the dictionary should be the objects themselves,
# and the values ​​should be a list in the format:
#
# [item, total]
#
# where item is an object of the ShopItem class; total - total number of identical objects (with identical hashes).
# Consider how to efficiently programmatically populate such a dictionary by iterating through the lst_in list once.


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    "System unit: 1500 75890.56",
    "Samsung monitor: 2000 34000",
    "keyboard: 200.44 545",
    "Samsung monitor: 2000 34000"
]
shop_items = {}
for string in lst_in:
    name, properties = string.split(":")
    shop_item = ShopItem(name, *map(float, properties.split()))
    shop_items.setdefault(shop_item, [shop_item, 0])[1] += 1


print(shop_items)
