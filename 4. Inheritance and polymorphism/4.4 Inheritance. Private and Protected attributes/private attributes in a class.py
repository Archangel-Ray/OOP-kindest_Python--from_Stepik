# Declare the class Animal (animal), whose objects are created by the command:
#
# an = Animal(name, kind, old)
#
# where name is the name of the animal (string); kind - type of animal (string); old - age (integer).
# Each object of this class must have corresponding private attributes: __name, __kind, __old.
#
# In the Animal class, property objects must be declared to change and read private attributes:
#
# name - to work with the private attribute __name;
# kind - to work with the private attribute __kind;
# old - to work with the private attribute __old.
#
# Create a list in the program called animals that contains three objects of class Animal with the following data:
#
# Vaska; yard cat; 5
# Rex; German Shepherd; 8
# Kesha; parrot; 3


class Animal:
    def __init__(self, name, kind, old):
        self.name = name
        self.kind = kind
        self.old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value


animals = [Animal("Vaska", "yard cat", 5),
           Animal("Rex", "German Shepherd", 8),
           Animal("Kesha", "parrot", 3)]
print(animals)
