# You are creating a project that intends to use lists of integers. To do this, your task is to create
# a class named ListInteger with a base class list and override three methods:
#
# __init__()
# __setitem__()
# append()
#
# so that the ListInteger list contains only integers.
# When trying to assign any other data type, throw an exception with the command:
#
# raise TypeError('only integer values ​​can be passed')
#
# An example of using the ListInteger class (do not write these lines in the program):
#
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError


class ListInteger(list):
    def __init__(self, list_args):
        for x in list_args:
            self.__check_type(x)
        super().__init__(list_args)

    @staticmethod
    def __check_type(x):
        if type(x) != int:
            raise TypeError("only integer values ​​can be passed")

    def __setitem__(self, key, value):
        self.__check_type(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.__check_type(value)
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5
