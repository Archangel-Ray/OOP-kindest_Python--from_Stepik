# An online store is being developed. Each product is supposed to be represented by the Thing class,
# the objects of which are created by the command:
#
# thing = Thing(name, price, weight)
#
# where name - product name (string); price - price (real number); weight - product weight (real number).
# Similar attributes are created in each object of this class: name, price, weight.
#
# The Thing class must be defined so that its objects can be used as dictionary keys, for example:
#
# d = {}
# d[thing] = thing
#
# And for each unique data set name, price, weight, its own unique keys must be formed.
#
# Next, you need to declare a DictShop dictionary class that inherits from the dict base class.
# In this new dictionary, only objects of class Thing can be keys.
# If you try to specify any other type, throw an exception with the command:
#
# raise TypeError('Only objects of class Thing can be keys')
#
# Objects of the DictShop class must be created with the commands:
#
# dict_things = DictShop() # empty dictionary
# dict_things = DictShop(things) # dictionary with things dictionary set
#
# where things is some dictionary. In the initializer, you should check that the thing argument is a dictionary,
# if not, then throw an exception:
#
# raise TypeError('argument must be a dictionary')
#
# And check that all keys are objects of the Thing class. If it's not, then throw an exception:
#
# raise TypeError('Only objects of class Thing can be keys')
#
# Additionally, in the DictShop class, override the method:
#
# __setitem__()
#
# with a check that the generated key is an object of the Thing class. Otherwise, throw an exception:
#
# raise TypeError('Only objects of class Thing can be keys')
#
# An example of using classes (do not write these lines in the program):
#
# th_1 = Thing('Ski', 11000, 1978.55)
# th_2 = Thing('Book', 1500, 256)
# dict_things = DictShop()
# dict_things[th_1] = th_1
# dict_things[th_2] = th_2
#
# for x in dict_things:
#     print(x.name)
#
# dict_things[1] = th_1 # TypeError exception


class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError("argument must be a dictionary")
        if things and not all(isinstance(key, Thing) for key in things):
            raise TypeError("keys can only be objects of class Thing")
        super().__init__(things)

    def __setitem__(self, key, value):
        if not isinstance(key, Thing):
            raise TypeError("keys can only be objects of class Thing")
        super().__setitem__(key, value)


th_1 = Thing('ski', 11000, 1978.55)
th_2 = Thing('book', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)

# dict_things[1] = th_1 # TypeError exception
