# You need to write a program for convenient handling of tables of the same type of data (numbers, strings,
# boolean values, etc.), that is, all table cells must represent one specified type.
#
# To do this, the program must declare three classes:
#
# TableValues ​​- for working with the table as a whole;
# CellInteger - for operations with integers;
# IntegerValue - is a data descriptor for working with integers.
#
# Let's start with the IntegerValue descriptor. It must be a data descriptor (that is, both for writing
# and reading values). If the value being assigned is not an integer, an exception must be thrown with the command:
#
# raise ValueError('only integer values ​​are possible')
#
# The following CellInteger class describes a single table cell for working with integers.
# This class must have a public attribute (class attribute):
#
# value - descriptor object, class IntegerValue.
#
# And objects of the CellInteger class must be created by the command:
#
# cell = CellInteger(start_value)
#
# where start_value is the starting value of the cell (default is 0 and stored in the cell via the value descriptor).
#
# Finally, objects of the last class TableValues ​​are created by the command:
#
# table = TableValues(rows, cols, cell=CellInteger)
#
# where rows, cols - number of rows and columns (integer); cell - a link to a class that describes how to work with
# individual table cells. If the cell parameter is not specified, then throw an exception with the command:
#
# raise ValueError('cell parameter not specified')
#
# Otherwise, a two-dimensional (nested) tuple named cells of size rows x cols is created in the table object
# of the TableValues ​​class, consisting of objects of the specified class (in this example, the CellInteger class).
#
# Also, in the TableValues ​​class, provide the ability to access a separate cell by its indices, for example:
#
# value = table[1, 2] # returns the value of the cell at index (1, 2)
# table[0, 0] = value # writes the new value to the cell (0, 0)
#
# Please note that the cell value should be returned immediately by indexes, and not an object of the CellInteger class.
# And the same with assigning a new value.
#
# An example of using classes (do not write these lines in the program):
#
# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
# table[1, 1] = 10
# table[0, 0] = 1.45 # throws a ValueError exception
#
# # output the table to the console
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()


class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError("only integer values ​​are possible")
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError("parameter cell is specified")

        self._rows = rows
        self._cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))

    def __check_index(self, index):
        r, c = index
        if type(r) != int or not (0 <= r < self._rows) or type(c) != int or not (0 <= c < self._cols):
            raise IndexError()

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45

for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
