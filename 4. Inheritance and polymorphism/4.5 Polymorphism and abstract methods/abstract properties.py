# Using the abc module, you can define not only abstract methods, but also abstract property objects.
# This is done as follows:
#
# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#     @abstractmethod
#     def go(self):
#         """Method to move the vehicle"""
#
#     @property
#     @abstractmethod
#     def speed(self):
#         """Abstract Property Object"""
#
# Using this information and the information about the abc module from feat 6,
# declare a base class named CountryInterface with the following abstract methods and properties:
#
# name - abstract property, country name (string);
# population - abstract property, population size (positive integer);
# square - abstract property, area of ​​the country (positive number);
#
# get_info() is an abstract method for getting country summary information.
#
# Based on the CountryInterface class, declare a child class Country whose objects are created by the command:
#
# country = Country(name, population, square)
#
# In the Country class itself, the following properties and methods of the base class must be overridden:
#
# name - property for reading country name (string);
# population - property for writing and reading population (positive integer);
# square - property for writing and reading country area (positive number);
#
# get_info() - method for getting country summary information as a string:
#
# "<name>: <area>, <population>"
#
# An example of using classes (you do not need to write these lines in the program):
#
# country = Country('Russia', 140000000, 324005489.55)
# name = country.name
# pop = country.population
# country.population = 150000000
# country.square = 354005483.0
# print(country.get_info()) # Russia: 354005483.0, 150000000
from abc import ABC, abstractmethod


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name, population, square):
        self.__name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        self.__square = value

    def get_info(self):
        return f"""{self.name}: {self.square}, {self.population}"""


country = Country("Russia", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())
