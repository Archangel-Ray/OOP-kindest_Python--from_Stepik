# Declare the class Money so that objects of this class can be created like this:
#
# my_money = Money(100)
# your_money = Money(1000)
# Here, when creating objects, the amount of money is specified, which should be stored in the local money
# property (attribute) of each instance of the class.
#
# P.S. You don't need to display anything on the screen.


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)
