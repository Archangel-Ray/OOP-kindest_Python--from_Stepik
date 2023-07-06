# Declare a class named Star, in objects of which only local attributes with names are allowed
# (the restriction is set through the __slots__ collection):
#
# _name - star name (string);
# _massa - mass of the star (any positive number); often measured in solar masses;
# _temp - temperature of the star's surface in Kelvin (any positive number).
#
# Objects of this class must be created with the command:
#
# star = Star(name, mass, temp)
#
# Based on the Star class, declare the following child classes:
#
# WhiteDwarf - white dwarf;
# YellowDwarf - yellow dwarf;
# RedGiant - red giant;
# Pulsar - a pulsar.
#
# In each object of these classes, only the following local attributes shall be allowed
# (in addition to the attributes of the Star base class):
#
# _type_star - star type name (string);
# _radius - star radius (any positive number); often measured in solar radii.
#
# Accordingly, objects of these classes must be created by the command:
#
# star = subclass_name(name, massa, temp, type_star, radius)
#
# Create the following star objects in the program:
#
# RedGiant: Aldebaran; 5; 3600; red giant; 45
# WhiteDwarf: Sirius A; 2.1; 9250; white dwarf; 2
# WhiteDwarf: Sirius B; 1; 8200; white dwarf; 0.01
# YellowDwarf: Sun; 1; 6000; yellow dwarf; 1
#
# Save all these objects as a list of stars. Then, using the isinstance() and filter() functions,
# form a new list called white_dwarfs, consisting only of white dwarfs (WhiteDwarf).


class Star:
    __slots__ = "_name", "_mass", "_temp"

    def __init__(self, name, mass, temp):
        self._name = name
        self._mass = mass
        self._temp = temp


class WhiteDwarf(Star):
    __slots__ = "_type_star", "_radius"

    def __init__(self, name, mass, temp, type_star, radius):
        super().__init__(name, mass, temp)
        self._type_star = type_star
        self._radius = radius


class YellowDwarf(Star):
    __slots__ = "_type_star", "_radius"

    def __init__(self, name, mass, temp, type_star, radius):
        super().__init__(name, mass, temp)
        self._type_star = type_star
        self._radius = radius


class RedGiant(Star):
    __slots__ = "_type_star", "_radius"

    def __init__(self, name, mass, temp, type_star, radius):
        super().__init__(name, mass, temp)
        self._type_star = type_star
        self._radius = radius


class Pulsar(Star):
    __slots__ = "_type_star", "_radius"

    def __init__(self, name, mass, temp, type_star, radius):
        super().__init__(name, mass, temp)
        self._type_star = type_star
        self._radius = radius


stars = [
    RedGiant("Aldebaran", 5, 3600, "red giant", 45),
    WhiteDwarf("Sirius A", 2.1, 9250, "white dwarf", 2),
    WhiteDwarf("Sirius B", 1, 8200, "white dwarf", 0.01),
    YellowDwarf("Sun", 1, 6000, "yellow dwarf", 1)
]
white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
print(*[a._name for a in white_dwarfs], sep="\n")
