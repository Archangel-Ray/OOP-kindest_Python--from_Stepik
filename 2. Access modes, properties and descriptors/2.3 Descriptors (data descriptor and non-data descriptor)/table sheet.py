# Declare a FloatValue data descriptor that sets and returns real values. When writing a real number, a check for
# a real data type must be performed. If the check fails, then throw an exception with the command:
#
# raise TypeError('Only real data type can be assigned.')
#
# Declare a Cell class that creates the value object of the FloatValue descriptor. And objects of the Cell class must
# be created with the command:
#
# cell = Cell(cell initial value)
#
# Declare a TableSheet class that creates a table with N rows and M columns as follows:
#
# table = TableSheet(N, M)
#
# Each cell of this table must be represented by an object of the Cell class, work with real numbers through the value
# object (the initial value must be 0.0).
#
# Each object of the TableSheet class must have a local attribute:
#
# cells - list (nested) of size N x M containing table cells (objects of class Cell).
#
# Create a table object of class TableSheet with table size N = 5, M = 3.
# Write numbers from 1.0 to 15.0 (in order) in this table.


class FloatValue:
    @classmethod
    def real_number_test(cls, number):
        if type(number) != float:
            raise TypeError("Only the real data type can be assigned.")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.real_number_test(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, start_value=0.0):
        self.value = start_value


class TableSheet:
    def __init__(self, N, M):
        self.cells = []
        for _ in range(N):
            self.cells.append([Cell() for _ in range(M)])


table = TableSheet(5, 3)
initial = 1.0
for line in range(5):
    for cell in range(3):
        table.cells[line][cell].value = initial
        initial += 1
print(table.__dict__)
