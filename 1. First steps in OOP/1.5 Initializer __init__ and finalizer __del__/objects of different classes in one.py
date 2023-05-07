# Declare the class Cart (basket) in the program, the objects of which are created by the command:
#
# cart = Cart()
#
# Each object of class Cart must have a local property goods - a list of objects for purchase (objects of classes
# Table, TV, Notebook and Cup). Initially, this list should be empty.
#
# Declare methods in the Cart class:
#
# add(self, gd) - adding to the cart the product represented by the object gd;
# remove(self, indx) - removal from the cart of goods by index indx;
# get_list(self) - getting goods from the cart as a list of strings:
#
# [' name_1 : price_1 ',
# ' name_2 : price_2 ',
# ...
# ' name_N : price_N ']
#
# Declare the following classes in the program to describe goods:
#
# Table - tables;
# TV - TVs;
# Notebook - laptops;
# Cup - mugs.
#
# Objects of these classes must be created with the command:
#
# gd = ClassName(name, price)
#
# Each product class object must contain local properties:
#
# name - name;
# price - price.
#
# Create a cart object of class Cart in the program. Add two TVs (TV), one table (Table), two laptops (Notebook)
# and one mug (Cup) to it. Think of names and prices yourself.
#
# P.S. You do not need to display anything on the screen, only create objects according to the specified requirements.


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{n.name}: {n.price}' for n in self.goods]


cart = Cart()
cart.add(TV('LG', 3216))
cart.add(TV('Philips', 654))
cart.add(Table('loft', 10))
cart.add(Notebook('ASUS', 123))
cart.add(Notebook('ASUS', 231))
cart.add(Cup('Thermo mug', 2))

print(cart.get_list())
