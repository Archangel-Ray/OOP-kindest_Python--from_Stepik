# You are creating an online store. To do this, you need to declare two classes:
#
# Shop - a class for managing the store as a whole;
# Product - a class for representing a single product.
#
# Shop class objects should be created with the command:
#
# shop = Shop(shop name)
#
# Each object of the Shop class must create a local property:
#
# goods - list of goods (initially the list is empty).
#
# And also declare methods in the class:
#
# add_product(self, product) - adding a new product to the store (to the end of the goods list);
# remove_product(self, product) - remove the product product from the store (from the goods list);
#
# Objects of the Product class should be created with the command:
#
# p = Product(name, weight, price)
#
# They should automatically generate local attributes:
#
# id - unique product identification number (automatically generated as a positive integer from 1 onwards);
# name - product name (string);
# weight - product weight (integer or real positive number);
# price - price (integer or real positive number).
#
# In the Product class, through magic methods (think about which ones), check the type of data assigned to local
# attributes of class objects (for example, id is an integer, name is a string, etc.). If the check fails, then
# throw an exception with the command:
#
# raise TypeError('Wrong type of data being assigned.')
#
# Also in the Product class, use the magic method(s) to disable the deletion of the local id attribute.
# When you try to do this, throw an exception:
#
# raise AttributeError('The id attribute cannot be removed.')
#
# An example of using classes (do not write these lines in the program):
#
# shop = Shop('Balakirev and K')
# book = Product('Python OOP', 100, 1024)
# shop.add_product(book)
# shop.add_product(Product('Python', 150, 512))
# for p in shop.goods:
# print(f'{p.name}, {p.weight}, {p.price}')


class Product:
    _id_instance = 1
    args_dic = {"name": (str, ), "weight": (float, int), "price": (float, int)}

    def __init__(self, name, weight, price):
        self.id = Product._id_instance
        Product._id_instance += 1
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.args_dic and type(value) in self.args_dic[key]:
            if (key == "weight" or key == "price") and value <= 0:
                raise TypeError("Wrong data type assigned.")
        elif key in self.args_dic:
            raise TypeError("Wrong data type assigned.")

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("The id attribute cannot be deleted.")


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


shop = Shop("Balakirev and K")
book = Product("Python OOP", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
