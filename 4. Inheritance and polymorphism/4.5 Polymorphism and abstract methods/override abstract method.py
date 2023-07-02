# You need to declare a ShopInterface base class with an abstract method:
#
# def get_id(self): ...
#
# In the method itself, an exception should be thrown with the command:
#
# raise NotImplementedError('the get_id method is not overridden in the class')
#
# There is no need to write an initializer in the ShopInterface class.
#
# Next, declare a child class ShopItem (from the base class ShopInterface), whose objects are created by the command:
#
# item = ShopItem(name, weight, price)
#
# where name - product name (string); weight - product weight (any positive number);
# price - item price (any positive number).
#
# In each object of the ShopItem class, local attributes with the names _name, _weight, _price
# and corresponding values ​​must be formed. Also, in objects of the ShopItem class,
# a local private attribute __id with a unique (for each product) integer value should be automatically generated.
#
# In the ShopItem class, you need to override the get_id() method of the base class so that it (the method)
# returns the value of the __id attribute.


class ShopInterface:
    def get_id(self):
        raise NotImplementedError("the get_id method is not overridden in the class")


class ShopItem(ShopInterface):
    __last_id = 0

    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = self.__last_id + 1
        ShopItem.__last_id += 1

    def get_id(self):
        return self.__id


product_1 = ShopItem("cheese", 200, 0.2)
product_2 = ShopItem("meat", 1000, 0.5)
product_3 = ShopItem("broccoli", 500, 0.01)
print(product_3.get_id())
print(product_2.get_id())
print(product_1.get_id())
