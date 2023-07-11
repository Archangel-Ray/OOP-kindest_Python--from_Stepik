# You are tasked with developing a TupleData class whose members can only be objects
# of the classes CellInteger, CellFloat, and CellString.
#
# First, in the program, you need to declare the CellInteger, CellFloat and CellString classes,
# the objects of which are created by the commands:
#
# cell_1 = CellInteger(min_value, max_value)
# cell_2 = CellFloat(min_value, max_value)
# cell_3 = CellString(min_length, max_length)
#
# where min_value, max_value - the minimum and maximum allowable value in the cell;
# min_length, max_length - the minimum and maximum allowable length of a string in a cell.
#
# In each object of these classes, local attributes with the names _min_value, _max_value or _min_length, _max_length
# and corresponding values ​​must be formed.
#
# Writing and reading the current value in a cell must be done through a property object with the name:
#
# value - to write and read the value in the cell (initially returns None).
#
# If at the time of writing the new value does not correspond to the range [min_value; max_value] or
# [min_length; max_length], then an exception is generated by the commands:
#
# raise CellIntegerException('value is out of range') # for CellInteger class objects
# raise CellFloatException('value is out of range') # for CellFloat objects
# raise CellStringException('string length out of range') # for CellString class objects
#
# All three exception classes must be inherited from the same general class:
#
# CellException
#
# Next, declare the TupleData class, whose objects are created by the command:
#
# ld = TupleData(cell_1, ..., cell_N)
#
# where cell_1, ..., cell_N are objects of classes CellInteger, CellFloat and CellString (in any order and any number).
#
# An individual cell must be accessed using the operator:
#
# value = ld[index] # read value from cell with index index
# ld[index] = value # write new value to cell with index index
#
# The index index is zero-based (for the first cell) and is an integer. If index is out of range [0; number of cells-1],
# then throw an IndexError exception.
#
# Also, the following functions and operators must be performed with objects of the TupleData class:
#
# res = len(ld) # returns the total number of elements (cells) in the ld object
# for d in ld: # loops through the cell values ​​of the ld object (values, not cell objects)
#     print(d)
#
# All these classes in the program can be used as follows:
#
# ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))
#
# try:
#     ld[0] = 1
#     ld[1] = 20
#     ld[2] = -5.6
#     ld[3] = 'Python OOP'
# except CellIntegerException as e:
#     print(e)
# except CellFloatException as e:
#     print(e)
# except CellStringException as e:
#     print(e)
# except CellException:
#     print('Error accessing cell')
# except Exception:
#     print('General error when working with a TupleData object')


class CellException(Exception): pass


class CellIntegerException(CellException): pass


class CellFloatException(CellException): pass


class CellStringException(CellException): pass


class Cell:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, "_" + key, value)
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self._is_valid(value)

    def _is_valid(self, value):
        raise NotImplementedError("the _is_valid method must be overridden")


class CellInteger(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellIntegerException("value is out of range")
        return value


class CellFloat(Cell):
    def __init__(self, min_value, max_value):
        super().__init__(min_value=min_value, max_value=max_value)

    def _is_valid(self, value):
        if not self._min_value <= value <= self._max_value:
            raise CellFloatException("value is out of range")
        return value


class CellString(Cell):
    def __init__(self, min_length, max_length):
        super().__init__(min_length=min_length, max_length=max_length)

    def _is_valid(self, value):
        if not self._min_length <= len(value) <= self._max_length:
            raise CellStringException("string length is out of range")
        return value


class TupleData:
    def __init__(self, *args):
        [self.__is_cell(x) for x in args]
        self.cells = args

    @staticmethod
    def __is_cell(x):
        if not isinstance(x, Cell):
            raise TypeError("Elements can only be objects of class Cell")

    def __getitem__(self, item):
        return self.cells[item].value

    def __setitem__(self, key, value):
        self.cells[key].value = value

    def __len__(self):
        return len(self.cells)

    def __iter__(self):
        for x in self.cells:
            yield x.value


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Cell access error")
except Exception:
    print("General error when working with a TupleData object")
