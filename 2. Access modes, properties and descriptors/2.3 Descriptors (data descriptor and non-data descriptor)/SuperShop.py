# You are starting to create an online store. To do this, the program declares the SuperShop class, the objects
# of which are created by the command:
#
# myshop = SuperShop(store name)
#
# The following local attributes must be formed in each object of the SuperShop class:
#
# name - store name (string);
# goods - a list of goods.
#
# Also, the SuperShop class should have methods:
#
# add_product(product) - adding a product to the store (at the end of the goods list);
# remove_product(product) - remove a product from the store (from the goods list).
#
# Here product is an object of the Product class that describes a specific product. The following descriptors should
# be declared in this class:
#
# name = StringValue(min_length, max_length) # min_length - minimum allowed string length;
# max_length - maximum allowed string length
# price = PriceValue(max_value) # max_value - the maximum allowable value
#
# Objects of the Product class will be created by the command:
#
# pr = Product(name, price)
#
# The StringValue and PriceValue classes are data descriptors. The StringValue class must check that a string type
# is assigned with a string length in the range [2; 50], i.e. min_length = 2, max_length = 50. The PriceValue class
# must check that a real or integer value is assigned in the range [0; 10000], i.e. max_value = 10000. If the checks
# fail, then the corresponding (old) values ​​should not change.
#
# An example of using the SuperShop class (you do not need to write these lines in the program):
#
# shop = SuperShop('Balakirev's')
# shop.add_product(Product('Python course', 0))
# shop.add_product(Product('Python OOP Course', 2000))
# for p in shop.goods:
# print(f'{p.name}: {p.price}')


class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name_shop):
        self.name = name_shop
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


shop = SuperShop("Balakirev's")
shop.add_product(Product("Python course", 0))
shop.add_product(Product("Python OOP Course", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
