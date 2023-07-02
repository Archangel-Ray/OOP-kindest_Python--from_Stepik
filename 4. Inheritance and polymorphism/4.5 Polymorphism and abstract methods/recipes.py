# Declare a class named Food, whose objects are created by the command:
#
# food = Food(name, weight, calories)
#
# where name - product name (string); weight - product weight (any positive number);
# calories - caloric value of the product (positive integer).
#
# Declare the following child classes with names:
#
# BreadFood - bread;
# SoupFood - soup;
# FishFood - fish.
#
# Objects of these classes must be created with the commands:
#
# bf = BreadFood(name, weight, calories, white) # white - True for white bread, False for others
# sf = SoupFood(name, weight, calories, dietary) # dietary - True for diet soup, False for other types
# ff = FishFood(name, weight, calories, fish) # fish - type of fish (salmon, perch, sardine, etc.)
#
# In each object of these child classes, the corresponding local attributes with names should be formed:
#
# BreadFood: _name, _weight, _calories, _white
# SoupFood: _name, _weight, _calories, _dietary
# FishFood: _name, _weight, _calories, _fish
#
# An example of using classes (you do not need to write these lines in the program):
#
# bf = BreadFood('Borodino bread', 34.5, 512, False)
# sf = SoupFood('Turtle Soup', 520, 890.5, False)
# ff = FishFood('Canned fish', 340, 1200, 'salmon')


class Food:
    def __init__(self, name, weight, calories):
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish


bf = BreadFood("Borodino bread", 34.5, 512, False)
sf = SoupFood("Turtle Soup", 520, 890.5, False)
ff = FishFood("Canned fish", 340, 1200, "salmon")
lst = [bf, sf, ff]
for x in lst:
    print(x.__dict__)
