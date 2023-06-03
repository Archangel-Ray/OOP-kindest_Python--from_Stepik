# You need to create a simple family budgeting program. To do this, declare two classes with names in the program:
#
# Budget - to manage the family budget;
# Item - item of budget expenses.
#
# Objects of the Item class must be created with the command:
#
# it = Item(name, money)
#
# where name is the name of the expense item; money - amount of expenses (real or integer).
#
# Accordingly, in each object of the Item class, local attributes name and money with the passed values ​​should be
# formed. Also, the following statements must be executed with objects of the Item class:
#
# s = it1 + it2 # sum for two expense items
#
# and in general:
#
# s = it1 + it2 + ... + itN # sum of N expense items
#
# When summing, the + operator must return a number - the calculated sum of the money attributes
# of the corresponding Item class objects.
#
# Objects of class Budget are created by the command:
#
# my_budget = Budget()
#
# And the Budget class itself should have the following methods:
#
# add_item(self, it) - adding an expense item to the budget (it is an object of the Item class);
# remove_item(self, indx) - removal of an expense item from the budget by its ordinal number indx (index: counted
# from zero);
# get_items(self) - returns a list of all expense items (a list of Item class objects).
#
# An example of using classes (you do not need to write these lines in the program):
#
# my_budget = Budget()
# my_budget.add_item(Item('Python OOP Course', 2000))
# my_budget.add_item(Item('Django Course', 5000.01))
# my_budget.add_item(Item('NumPy course', 0))
# my_budget.add_item(Item('C++ course', 1500.10))
#
# # calculate total expenses
# s = 0
# for x in my_budget.get_items():
# s = s + x


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other.money

    def __radd__(self, other):
        return other + self.money


class Budget:
    def __init__(self):
        self.budget_list = []

    def add_item(self, it):
        self.budget_list.append(it)

    def remove_item(self, indx):
        if indx < len(self.budget_list):
            self.budget_list.pop(indx)

    def get_items(self):
        return self.budget_list


it1 = Item("Python OOP Course", 2000)
it2 = Item("Django course", 5000.01)
s = it1 + it2
print(s)
my_budget = Budget()
my_budget.add_item(Item("Python OOP Course", 2000))
my_budget.add_item(Item("Django course", 5000.01))
my_budget.add_item(Item("NumPy course", 0))
my_budget.add_item(Item("C++ course", 1500.10))
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
