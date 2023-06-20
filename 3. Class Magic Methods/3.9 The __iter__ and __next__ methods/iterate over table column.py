# Now, you need to develop an iterator that will iterate over the specified columns of the two-dimensional list.
# The list is a two-dimensional table of data:
#
# lst = [[x11, x12, ..., x1N],
#        [x21, x22, ..., x2N],
#        ...
#        [xM1, xM2, ..., xMN]
#       ]
#
# To do this, it is necessary to declare a class named IterColumn in the program,
# the objects of which are created by the command:
#
# it = IterColumn(lst, column)
#
# where lst is a reference to a two-dimensional list; column - index of the iterated column (based on 0).
#
# Then, with objects of the IterColumn class, the following operations should be available:
#
# it = IterColumn(lst, 1)
# for x in it: # iterate over all elements of the list column: x12, x22, ..., xM2
#       print(x)
#
# it_iter = iter(it)
# x = next(it_iter)


class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for row in self.lst:
            yield row[self.column]


ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
it = IterColumn(ls, 1)
for x in it:
    print(x)

it_iter = iter(it)
x = next(it_iter)
