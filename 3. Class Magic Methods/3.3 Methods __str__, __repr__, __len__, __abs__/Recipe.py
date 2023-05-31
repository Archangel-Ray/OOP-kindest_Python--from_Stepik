# Declare a Recipe class to represent recipes. The individual ingredients of a recipe must be defined by the
# Ingredient class. Objects of these classes must be created with the commands:
#
# ing = Ingredient(name, volume, measure)
# recipe = Recipe()
# recipe = Recipe(ing_1, ing_2,..., ing_N)
#
# where ing_1, ing_2,..., ing_N are objects of class Ingredient.
#
# Local attributes must be created on each object of the Ingredient class:
#
# name - ingredient name (string);
# volume - the volume of the ingredient in the recipe (real number);
# measure - ingredient volume unit (string), for example, liter, teaspoon, gram, pieces, etc.;
#
# The following function should work with objects of the Ingredient class:
#
# str(ing) # name: volume, units rev.
#
# and return a string representation of the object in the format:
#
# 'name: volume, unit of measure.'
#
# For example:
#
# ing = Ingredient('Salt', 1, 'tbsp')
# s = str(ing) # Salt: 1, tbsp
#
# The Recipe class must have the following methods:
#
# add_ingredient(ing) - adding a new ingredient ing (an object of the Ingredient class) to the recipe (at the end);
# remove_ingredient(ing) - remove an ingredient by the ing object (an object of the Ingredient class) from the recipe;
# get_ingredients() - get a tuple of Ingredient objects of the current recipe.
#
# Also with objects of class Recipe the function should be supported:
#
# len(recipe) - Returns the number of ingredients in the recipe.
#
# An example of using classes (you do not need to write these lines in the program):
#
# recipe = Recipe()
# recipe.add_ingredient(Ingredient('Salt', 1, 'tablespoon'))
# recipe.add_ingredient(Ingredient('Flour', 1, 'kg'))
# recipe.add_ingredient(Ingredient('Lamb meat', 10, 'kg'))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.list_ingredients = list(args)

    def add_ingredient(self, ing):
        self.list_ingredients.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.list_ingredients:
            self.list_ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.list_ingredients)

    def __len__(self):
        return len(self.list_ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Salt", 1, "tablespoon"))
recipe.add_ingredient(Ingredient("Flour", 1, "kg"))
recipe.add_ingredient(Ingredient("Lamb meat", 10, "kg"))
print(recipe.get_ingredients())
print(len(recipe))
ing = Ingredient('Salt', 1, 'tbsp')
s = str(ing)
recipe.add_ingredient(ing)
recipe.remove_ingredient(ing)
print(len(recipe))
