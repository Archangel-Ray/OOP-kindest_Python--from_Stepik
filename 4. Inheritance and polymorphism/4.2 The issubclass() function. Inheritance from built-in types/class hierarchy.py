# Declare the following classes without content in the program (use the pass statement):
#
# Protists, Plants, Animals, Mosses, Flowering, Worms, Mammals, Human, Monkeys
#
# and build the inheritance scheme according to the following hierarchy of the tree of life:
#
# Then, declare the classes in the program:
#
# Monkey - inherited from Monkeys and used to describe monkeys;
# Person - inherited from Human and serves to describe a person;
# Flower - inherited from Flowering and used to describe a flower;
# Worm - inherited from Worms and is used to describe worms.
#
# Objects of these classes must be created with the commands:
#
# obj = Monkey(name, weight, old)
# obj = Person(name, weight, old)
# obj = Flower(name, weight, old)
# obj = Worm(name, weight, old)
#
# where name is the name (or name) of the object (string); weight - weight (real number); old - age (integer).
# In each object of any of these classes, the corresponding attributes must be created: name, weight, old.
#
# Create the following objects in the program and save them as a lst_objs list:
#
# Monkey: 'monkey', 30.4, 7
# Monkey: 'chimpanzee', 24.6, 8
# Person: 'Balakirev', 88, 34
# Person: 'High Priest', 67.5, 45
# Flower: 'Tulip', 0.2, 1
# Flower: 'Rose', 0.1, 2
# Worm: 'worm', 0.01, 1
# Worm: 'worm 2', 0.02, 1
#
# Then, using the isinstance() functions and the List comprehensions generator,
# form the following lists from the specified objects:
#
# lst_animals - all objects related to animals (Animals);
# lst_plants - all objects related to plants (Plants);
# lst_mammals - all objects related to mammals (Mammals).


class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


lst_objs = [
    Monkey("marmoset", 30.4, 7),
    Monkey("chimpanzee", 24.6, 8),
    Person("Balakirev", 88, 34),
    Person("hierophant", 67.5, 45),
    Flower("tulip", 0.2, 1),
    Flower("rose", 0.1, 2),
    Worm("worm", 0.01, 1),
    Worm("worm 2", 0.02, 1)
]

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
print([obj.name for obj in lst_animals],
      [obj.__dict__ for obj in lst_plants],
      [obj.name for obj in lst_mammals],
      sep="\n")
