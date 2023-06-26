# It is known that only the same objects (tuples) can be added with objects of the tuple class. For example:
#
# t1 = (1, 2, 3)
# t2 = t1 + (4, 5) # (1, 2, 3, 4, 5)
# If we try to add any other iterable, like a list:
#
# t2 = t1 + [4, 5]
# then an error will occur. It is proposed to fix this functionality and create your own Tuple class,
# inherited from the base tuple class and supporting the operator:
#
# t1 = Tuple(iter_obj)
# t2 = t1 + iter_obj # a new Tuple object is created with a new (connected) dataset
#
# where iter_obj is any iterable object (list, dictionary, string, set, tuple, etc.)
#
# An example of using the class (do not write these lines in the program):
#
# t = Tuple([1, 2, 3])
# t = t + 'Python'
# print(t) # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# t = (t + 'Python') + 'OOP'


class Tuple(tuple):
    def __add__(self, other):
        return Tuple(tuple(self) + tuple(other))


t = Tuple([1, 2, 3])
t = t + t
t = t + "Python"
t = (t + "Python") + "OOP"
print(t)
