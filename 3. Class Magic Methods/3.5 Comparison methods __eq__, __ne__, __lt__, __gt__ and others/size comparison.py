# Declare a class Dimensions (dimensions) with attributes:
#
# MIN_DIMENSION = 10
# MAX_DIMENSION = 10000
#
# Each object of class Dimensions must be created with the command:
#
# d3 = Dimensions(a, b, c) # a, b, c - overall dimensions
#
# The values ​​a, b, c must be stored in the local private attributes __a, __b, __c of objects of this class.
#
# To change and access private attributes in the Dimensions class, property objects (property)
# with the names: a, b, c must be declared. Moreover, at the moment of assigning a new value,
# a check should be made if the number falls into the range [MIN_DIMENSION; MAX_DIMENSION].
# If the number does not fit, then it is ignored and the existing value is not changed.
#
# The following comparison operators must work with Dimensions objects:
#
# dim1 = dim2 # True if the volume of dim1 is greater than or equal to the volume of dim2
# dim1 dim2 # True if the volume of dim1 is greater than the volume of dim2
# dim1 = dim2 # True if the volume of dim1 is less than or equal to the volume of dim2
# dim1 dim2 # True if the volume of dim1 is less than the volume of dim2
#
# Declare another class in the program called ShopItem (goods), whose objects are created by the command:
#
# item = ShopItem(name, price, dim)
#
# where name - product name (string); price - item price (integer or real number);
# dim - product dimensions (object of Dimensions class).
#
# Local attributes must be created in each object of the ShopItem class:
#
# name - product name;
# price - item price;
# dim - product dimensions (object of Dimensions class).
#
# Create a list named lst_shop of four products with the following data:
#
# - sneakers; 1024; (40, 30, 120)
# - umbrella; 500.24; (10, 20, 50)
# - fridge; 40000; (2000, 600, 500)
# - stool; 2000.99; (500, 200, 200)
#
# Generate a new list lst_shop_sorted with the items in the lst_shop list sorted in ascending order
# of volume (dimensions), using the standard Python sorted() function and its key parameter to configure sorting.
# The old lst_shop list should remain unchanged.


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __check(self, value):
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return value

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value if self.__check(value) else None

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value if self.__check(value) else None

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value if self.__check(value) else None

    def __ge__(self, other):
        x = self.a * self.b * self.c
        y = other.a * other.b * other.c
        return x >= y

    def __gt__(self, other):
        return self.a * self.b * self.c > other.a * other.b * other.c

    def __le__(self, other):
        x = self.a * self.b * self.c
        y = other.a * other.b * other.c
        return x <= y

    def __lt__(self, other):
        return self.a * self.b * self.c < other.a * other.b * other.c


class ShopItem:
    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem("sneakers", 1024, Dimensions(40, 30, 120)),
            ShopItem("umbrella", 500.24, Dimensions(10, 20, 50)),
            ShopItem("fridge", 40000, Dimensions(2000, 600, 500)),
            ShopItem("stool", 2000.99, Dimensions(500, 200, 200))]
print(lst_shop[0].dim >= lst_shop[1].dim)
print(lst_shop[0].dim > lst_shop[1].dim)
print(lst_shop[0].dim <= lst_shop[1].dim)
print(lst_shop[0].dim < lst_shop[1].dim)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(lst_shop)
