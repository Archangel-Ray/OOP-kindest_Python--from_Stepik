# You are given the task of developing an iterator for sequentially iterating over the elements
# of nested (two-dimensional) lists of the following structure:
#
# lst = [[x00],
#        [x10, x11],
#        [x20, x21, x22],
#        [x30, x31, x32, x33],
#        ...
#       ]
# To do this, it is necessary to declare a class in the program with the name TriangleListIterator,
# whose objects are created by the command:
#
# it = TriangleListIterator(lst)
#
# where lst is a reference to the list being iterated over.
#
# Then, the following operations should be available on objects of the TriangleListIterator class:
#
# for x in it: # iterate over all elements of the list: x00, x10, x11, x20, ...
#       print(x)
#
# it_iter = iter(it)
# x = next(it_iter)
#
# The iterator must iterate over the elements of the list in the specified triangular shape.
# Even if a rectangular table (nested list) is passed to the iterator, its enumeration must still be carried
# out along the triangle. If this is not possible (due to the structure of the list), then the error IndexError:
# index out of range should naturally occur.


class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        for i in range(len(self.lst)):
            for j in range(i+1):
                yield self.lst[i][j]


ls = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
ls_one = [x for row in ls for x in row]
t = TriangleListIterator(ls)
it = iter(t)
while True:
    print(next(it), end=", ")
