# The program needs to declare classes for working with wallets in different currencies:
#
# MoneyR - for ruble wallets
# MoneyD - for dollar wallets
# MoneyE - for euro wallets
#
# Objects of these classes can be created with the commands:
#
# rub = MoneyR() # with zero balance
# dl = MoneyD(1501.25) # with a balance of $1501.25
# euro = MoneyE(100) # with a balance of 100 euros
#
# Local attributes must be formed in each object of these classes:
#
# __cb - reference to the CentralBank class (central bank, initially None);
# __volume - the amount of funds in the wallet (if not specified, then 0).
#
# Also, the MoneyR, MoneyD and MoneyE classes should have property objects for working with local attributes:
#
# cb - for changing and reading data from the __cb variable;
# volume - to change and read data from the __volume variable.
#
# Class objects must support the following comparison operators:
#
# rub < dl
# dl >= euro
# rub == euro # values ​​are compared at the current central bank rate with an error of 0.1 (plus or minus)
# euro > rub
#
# When implementing comparison operators, the corresponding __volume values ​​are read from the compared objects
# and converted to the ruble equivalent in accordance with the exchange rate of the central bank.
#
# In order for each object of the MoneyR, MoneyD and MoneyE classes to 'know' the current quotes, it is necessary
# to declare one more CentralBank class in the program. Objects of the CentralBank class should not be created
# (prohibited) when executing the command:
#
# cb = CentralBank()
#
# it should just return None. And in the class itself there must be an attribute:
#
# rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
# Here the numbers (in the dictionary values) are the exchange rate against the dollar.
#
# Also, CentralBank should have a class-level method:
#
# register(cls, money) - for registering objects of classes MoneyR, MoneyD and MoneyE.
#
# When registered, the __cb value of the money object must refer to the CentralBank class. Through this variable,
# the object has the ability to access the rates attribute of the CentralBank class and take the necessary quotes.
#
# If the wallet is not registered, then an exception should be thrown during comparison operations:
#
# raise ValueError("Unknown exchange rate.")
#
# An example of using classes (you do not need to write these lines in the program):
#
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
# r = MoneyR(45000)
# d = MoneyD(500)
#
# CentralBank.register(r)
# CentralBank.register(d)
#
# if r > d:
#     print("not bad")
# else:
#     print("need to push")


class Money:
    type_money = None
    EPS = 0.1

    def __init__(self, arg=0):
        self.cb = None
        self.volume = arg

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError("Unknown exchange rate.")
        if self.type_money is None:
            raise ValueError("Wallet type unknown")
        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]
        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volumes(other)
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = "rub"


class MoneyD(Money):
    type_money = "dollar"


class MoneyE(Money):
    type_money = "euro"


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return

    @classmethod
    def register(cls, money):
        money.cb = cls


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("not bad")
else:
    print("need to push")
