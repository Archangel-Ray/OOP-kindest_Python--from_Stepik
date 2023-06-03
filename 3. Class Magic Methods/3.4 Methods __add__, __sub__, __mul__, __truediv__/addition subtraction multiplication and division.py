# Declare a class named ListMath whose objects can be created with commands:
#
# lst1 = ListMath() # empty list
# lst2 = ListMath([1, 2, -5, 7.68]) # list with initial values
#
# Objects of the ListMath class should select only integers and real numbers as values ​​for the elements of the list,
# and ignore the rest (if they are specified in the list). For example:
#
# lst = ListMath([1, 'abc', -5, 7.68, True]) # ListMath: [1, -5, 7.68]
#
# Each object of the ListMath class must have a public attribute:
#
# lst_math - link to the current list of the object (each object has its own list).
#
# The following operators should also work with objects of the ListMath class:
#
# lst = lst + 76 # add each number in the list to a specific number
# lst = 6.5 + lst # add each number in the list to a specific number
# lst += 76.7 # add each number in the list to a specific number
# lst = lst - 76 # subtract a certain number from each number in the list
# lst = 7.0 - lst # subtraction from the number of each number in the list
# lst -= 76.3
# lst = lst * 5 # multiply each number in the list by the specified number (5 in this case)
# lst = 5 * lst # multiply each number in the list by the specified number (5 in this case)
# lst *= 5.54
# lst = lst / 13 # divide each number in the list by the specified number (in this case, 13)
# lst = 3 / lst # dividing the number by each element of the list
# lst /= 13.0
#
# When using binary operators +, -, *, /, new objects of the ListMath class with new lists must be formed,
# the old lists do not change.
#
# When using the +=, -=, *=, /= operators, the values ​​must change within the list of the current
# object (no new object is created).


class ListMath:
    def __init__(self, new_list=None):
        self.lst_math = new_list if new_list and type(new_list) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    def __add__(self, other):
        return ListMath([num + other for num in self.lst_math])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return ListMath([num - other for num in self.lst_math])

    def __rsub__(self, other):
        return ListMath([other - num for num in self.lst_math])

    def __mul__(self, other):
        return ListMath([num * other for num in self.lst_math])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return ListMath([num / other for num in self.lst_math])

    def __rtruediv__(self, other):
        return ListMath([other / num for num in self.lst_math])

    def __iadd__(self, other):
        self.lst_math = [num + other for num in self.lst_math]
        return self

    def __isub__(self, other):
        self.lst_math = [num - other for num in self.lst_math]
        return self

    def __imul__(self, other):
        self.lst_math = [num * other for num in self.lst_math]
        return self

    def __itruediv__(self, other):
        self.lst_math = [num / other for num in self.lst_math]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])
lst = lst + 76
lst = 6.5 + lst
lst += 76.7
lst = lst - 76
lst = 7.0 - lst
lst -= 76.3
lst = lst * 5
lst = 5 * lst
lst *= 5.54
lst = lst / 13
lst = 3 / lst
lst /= 13.0
