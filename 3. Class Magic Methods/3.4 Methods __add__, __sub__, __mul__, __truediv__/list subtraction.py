# It is known that in Python we can join two lists together using the + operator:
#
# lst = [1, 2, 3] + [4.5, -3.6, 0.78]
#
# But there is no implementation of the - operator, which would remove from the list the corresponding values ​​
# of the subtracted list, as shown in the example:
#
# # [2, 3, 4] (the order of the remaining elements of the list must be preserved)
# lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1]
#
# Let's fix this and create such functionality.
# To do this, you need to declare a class named NewList, whose objects are created by the commands:
#
# lst = NewList() # empty list
# lst = NewList([-1, 0, 7.56, True]) # list with initial values
#
# mplement a subtraction operator for this class so that you can perform the following actions on objects
# of the NewList class:
#
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
#
# You also need to declare a method in the NewList class:
#
# get_list() - to return the resulting list of the NewList class object
#
# For example:
#
# lst = res_2.get_list() # [1, 2, 3]


class NewList:
    def __init__(self, *args):
        self.list_arg = []
        if len(args) != 0:
            self.list_arg = args[0]

    def get_list(self):
        return self.list_arg

    @staticmethod
    def __diff_list(lst_1, lst_2):
        if len(lst_2) == 0:
            return lst_1
        sub = lst_2[:]
        return [x for x in lst_1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self.list_arg, other_list))

    def __rsub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError
        return NewList(self.__diff_list(other, self.list_arg))


lst_1 = NewList()
lst_2 = NewList([-1, 0, 7.56, True])
lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
