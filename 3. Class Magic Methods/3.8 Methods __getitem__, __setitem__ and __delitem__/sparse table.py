# You need to describe very large and sparse data tables (with many gaps) in the program. To do this,
# it is proposed to declare the SparseTable class, the objects of which are created by the command:
#
# st = SparseTable()
#
# In each object of this class, local public attributes must be created:
#
# rows - total number of table rows (initial value 0);
# cols - total number of table columns (initial value 0).
#
# Methods must be declared in the SparseTable class itself:
#
# add_data(row, col, data) - adding data data (object of class Cell) to the table by indexes row,
# col (non-negative integers);
# remove_data(row, col) - removal of a cell (object of the Cell class) with indices (row, col).
#
# When deleting/adding a new cell, the rows and cols attributes of the SparseTable class object should be automatically
# recalculated. If an attempt is made to delete a non-existent cell, then an exception should be thrown:
#
# raise IndexError('cell with specified indexes does not exist')
#
# Table cells are objects of the Cell class, which are created by the command:
#
# data = cell(value)
#
# where value is the cell data (any type).
#
# Cells should be stored in a dictionary, the keys of which are indices (tuple) i, j, and the values
# ​​are objects of the Cell class.
#
# Also, the following commands must be executed with objects of the SparseTable class:
#
# res = st[i, j] # getting data from the table by indexes (i, j)
# st[i, j] = value # writing new data by indexes (i, j)
#
# Reading data is only possible for existing cells. If there are no cells with the specified indexes,
# then generate an exception with the command:
#
# raise ValueError('there is no data at the specified indices')
#
# When writing new values, they should be changed in an existing cell or a new one should be added if the cell
# with indices (i, j) is not in the table. (Don't forget to recalculate the rows and cols attributes as you do this.)
#
# An example of using classes (do not write these lines in the program):
#
# st = SparseTable()
# st.add_data(2, 5, Cell('cell_25'))
# st.add_data(0, 0, Cell('cell_00'))
# st[2, 5] = 25 # change the value of an existing cell
# st[11, 7] = 'cell_117' # create a new cell
# print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols) # 12, 8 is the total number of rows and columns in the table
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) #IndexError


class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.table = {}

    def update_index(self):
        self.rows = max(key[0] for key in self.table) + 1
        self.cols = max(key[1] for key in self.table) + 1

    def add_data(self, row, col, data):
        self.table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.table[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError("cell with specified indexes does not exist")

    def __getitem__(self, item):
        try:
            return self.table[(item[0], item[1])].value
        except KeyError:
            raise ValueError("data for the indicated indexes are not available")

    def __setitem__(self, key, value):
        if (key[0], key[1]) not in self.table:
            self.table[(key[0], key[1])] = Cell(value)
            self.update_index()
        else:
            self.table[(key[0], key[1])] = Cell(value)


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25
st[11, 7] = 'cell_117'
print(st[0, 0])
st.remove_data(2, 5)
print(st.rows, st.cols)
# val = st[2, 5]
# st.remove_data(12, 3)
