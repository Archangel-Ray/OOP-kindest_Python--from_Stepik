# Inheritance is often used to move the common code of subclasses into a base class. Let's make an example.
# Declare in the program the base class Animal, whose objects can be created with the command:
#
# an = Animal(name, old)
#
# where name is the name of the animal (string); old - the age of the animal (integer).
# The same local attributes (name and old) must be created on class objects.
#
# Next, declare a child class (from the base Animal) named Cat, whose objects are created by the command:
#
# cat = Cat(name, old, color, weight)
#
# where name, old are the same parameters as in the base class; color - cat color (string);
# weight - the weight of the cat (any positive number).
#
# In objects of the Cat class, local attributes should be automatically formed: name, old, color, weight.
# The formation of the name, old attributes must be performed by the base class initializer.
#
# By analogy, declare another child class Dog, whose objects are created by the command:
#
# dog = Dog(name, old, breed, size)
#
# here name, old are the same parameters as in the base class; breed - dog breed (string);
# size is a tuple in the format (height, length) height and length are numbers.
#
# In objects of class Dog, by analogy, local attributes should be formed: name, old, breed, size.
# The initializer of the base class is responsible for the formation of the name, old attributes.
#
# Finally, in the Cat and Dog classes, declare a method:
#
# get_info() - to get information about an animal.
#
# This method should return a string in the format:
#
# 'name: old, other parameters separated by commas '
#
# For example, for the following object of class Cat:
#
# cat = Cat('cat', 4, 'black', 2.25)
#
# the get_info method should return the string:
#
# 'cat: 4, black, 2.25'


class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self):
        data = list(self.__dict__.values())
        return f"{data[0]}: {', '.join(map(str, data[1:]))}"


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f'''{self.name}: {self.old}, {self.color}, {self.weight}'''


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f'''{self.name}: {self.old}, {self.breed}, {self.size}'''


cat = Cat('tomcat', 4, 'black', 2.25)
print(cat.get_info())
