# A warehouse accounting program is being created. Each item in the warehouse must be described by the Thing base class.
# Objects of this class are created by the command:
#
# th1 = Thing(name, weight)
#
# where name - item name (string); weight - item weight (real number).
#
# To describe each specific type of item, child classes are created (based on the base Thing):
#
# ArtObject - to represent art objects;
# Computer - for system blocks of computers;
# Auto - for cars.
#
# Objects of these classes are created by the commands:
#
# obj = ArtObject(name, weight, author, date) # author - author (string); date - creation date (string)
# obj = Computer(name, weight, memory, cpu) # memory - memory size (integer); cpu - processor type (string)
# obj = Auto(name, weight, dims) # dims - dimensions, tuple (width, length, height) - real or integer numbers
#
# Based on the Auto class, child classes Mercedes and Toyota are created,
# the objects of which are defined by the commands:
#
# auto = Mercedes(name, weight, dims, model, old) # model - model (string); old - usage time, in years (integer)
# auto = Toyota(name, weight, dims, model, wheel) # model - model (string); wheel - steering wheel type:
# True - left-hand drive, False - right-hand drive
#
# All class objects must have corresponding local attributes: name, weight, etc.
#
# Attribute initialization should be done in the appropriate classes (there should be no code duplication).


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = author
        self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = memory
        self.cpu = cpu


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        self.model = model
        self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        self.model = model
        self.wheel = wheel


corolla = Toyota("Car", 2000, (1695, 3940, 1500), "Corolla", True)
for x, y in corolla.__dict__.items():
    print(f"{x}: {y};")
