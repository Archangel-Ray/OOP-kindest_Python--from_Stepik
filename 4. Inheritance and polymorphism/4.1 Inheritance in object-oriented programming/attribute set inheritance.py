# Sometimes inheritance is used to give subclass objects a certain set of attributes. Let's make an example.
#
# Suppose you are developing a program for an online store. This store can have both real (physical) goods
# and electronic ones. These two groups obviously need a different set of attributes:
#
# - for real physical goods: id, name, price, weight, dims
#
# where id - product identifier (integer);
# name - product name (string);
# price - product price (real number);
# weight - product weight (real number);
# dims = (lenght, width, depth) - length, width, depth - product dimensions (real numbers);
#
# - for electronic goods: id, name, price, memory, frm
#
# where id - product identifier (integer); name - product name (string); price - product price (real number);
# memory - occupied size (in bytes - an integer); frm - data format (string: pdf, docx, etc.)
#
# Since all products can be mixed, we want each object (for a product) to have all the attributes:
#
# id, name, price, weight, dims, memory, frm
#
# with initial values ​​of None. And already, then, specific data will be assigned to the necessary ones.
#
# To implement this logic, declare in the program a base class named Thing (thing, subject),
# whose objects can be created by the command:
#
# th = Thing(name, price)
#
# And the id attribute should be generated automatically and be unique for each product
# (for example, you can increase by one for each new object).
#
# Objects of the Thing class must form a complete set of local attributes (id, name, price, weight, dims, memory, frm)
# with the None value, except for the following attributes: id, name, price.
#
# Next, we need to declare two child classes:
#
# Table - for tables;
# ElBook - for electronic books.
#
# Objects of these classes must be created with the commands:
#
# table = Table(name, price, weight, dims)
# book = ElBook(name, price, memory, frm)
#
# Moreover, the name, price (as well as id) attributes should be initialized in the base class,
# because they are common to all products. The rest of the attributes must either be set to None if not used,
# or be initialized to specific values ​​already in child classes.
#
# Finally, in the Thing base class, declare a method:
#
# get_data() - to get a tuple in the format (id, name, price, weight, dims, memory, frm)
#
# An example of using classes (you do not need to write these lines in the program):
#
# table = Table('Round', 1024, 812.55, (700, 750, 700))
# book = ElBook('Python OOP', 2000, 2048, 'pdf')
# print(*table.get_data())
# print(*book.get_data())


class Thing:
    __instance_id = 0
    __attrs = ("id", "name", "price", "weight", "dims", "memory", "frm")

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.__get_id()
        self.weight = self.dims = self.memory = self.frm = None

    @classmethod
    def __get_id(cls):
        Thing.__instance_id += 1
        return Thing.__instance_id

    def get_data(self):
        return tuple(getattr(self, name) for name in self.__attrs)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("round", 1024, 812.55, (700, 750, 700))
book = ElBook("Python OOP", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
