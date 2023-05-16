# Declare a class named Money and define the following variables and methods in it:
#
# - private local variable money (integer) for storing the amount of money (its own for each object of the Money class);
# - public method set_money(money) for passing a new value to the private local variable money (the change is performed
# only if the check_money(money) method returns True);
# - public method get_money() to get the current amount of funds (money);
# - public method add_money(mn) for adding funds from the mn object of the Money class to the funds
# of the current object;
# - private class method check_money(money) for checking the correct amount of funds in the money parameter
# (returns True if the value is correct and False otherwise).
#
# Validation is performed according to the criterion: the money parameter must be an integer greater
# than or equal to zero.


class Money:
    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @classmethod
    def __check_money(cls, money):
        return type(money) == int and money >= 0


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
print(m1, m2)
