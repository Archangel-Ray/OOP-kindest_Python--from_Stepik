# Declare a class Matrix (matrix) for operations with matrices. Objects of this class must be created with the command:
#
# m1 = Matrix(rows, cols, fill_value)
#
# where rows, cols are the number of rows and columns of the matrix; fill_value - the initial value
# of the matrix elements to be filled (must be a number: integer or real). If not numbers are passed as arguments,
# then throw an exception:
#
# raise TypeError('arguments rows, cols are integers; fill_value is an arbitrary number')
#
# You can also create objects with the command:
#
# m2 = Matrix(list2D)
#
# where list2D is a two-dimensional list (rectangular) consisting of numbers (integer or real). If the list2D list
# is not rectangular, or at least one of its elements is not a number, then throw an exception with the command:
#
# raise TypeError('list must be rectangular, consisting of numbers')
#
# For objects of the Matrix class, the following commands must be executed:
#
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # return the first element of the matrix
# matrix[indx1, indx2] = value # matrix element with indices (indx1, indx2) is assigned a new value
#
# If, as a result of the assignment, the data type does not match the number, then throw an exception with the command:
#
# raise TypeError('matrix values ​​must be numbers')
#
# If invalid matrix indexes are specified (should be integers from 0 to the size of the matrix),
# then throw an exception:
#
# raise IndexError('invalid index values')
#
# Also, with objects of the Matrix class, the following operators must be performed:
#
# matrix = m1 + m2 # addition of the corresponding values ​​of the elements of the matrices m1 and m2
# matrix = m1 + 10 # add a number to all elements of matrix m1
# matrix = m1 - m2 # subtract the corresponding values ​​of the elements of the matrices m1 and m2
# matrix = m1 - 10 # subtract a number from all elements of matrix m1
#
# In all these operations, a new matrix with the corresponding values ​​must be formed.
# If the dimensions of the matrices do not match (different at least along one axis),
# then generate an exception with the command:
#
# raise ValueError('Operations are only possible with matrices of equal size')
#
# An example to understand the use of indexes (these lines do not need to be written in the program):
#
# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] #4


class Matrix:
    def __init__(self, rows_or_list, cols=0, fill_value=0):
        if type(rows_or_list) == list:
            self.rows = len(rows_or_list)
            self.cols = len(rows_or_list[0])
            if not all(len(r) == self.cols for r in rows_or_list) or \
                    not all(self.__is_digit(x) for row in rows_or_list for x in row):
                raise TypeError("the list must be rectangular, consisting of numbers")
            self.lst = rows_or_list
        else:
            if type(rows_or_list) != int or type(cols) != int or type(fill_value) not in (int, float):
                raise TypeError("arguments rows, cols are integers; fill_value - arbitrary number")
            self.rows = rows_or_list
            self.cols = cols
            self.lst = [[fill_value for _ in range(cols)] for _ in range(rows_or_list)]

    @staticmethod
    def __is_digit(x):
        return type(x) in (int, float)

    def __check_index(self, index):
        if not (0 <= index[0] < self.rows) or not (0 <= index[1] < self.cols):
            raise IndexError("invalid index values")

    def __getitem__(self, item):
        self.__check_index(item)
        return self.lst[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not self.__is_digit(value):
            raise TypeError("matrix values ​​must be numbers")
        self.lst[key[0]][key[1]] = value

    def __check_dimencions(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("operations are possible only with matrices of equal sizes")

    def __add__(self, other):
        if type(other) == type(self):
            self.__check_dimencions(other)
            return Matrix([[self[i, j] + other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] + other for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        if type(other) == type(self):
            self.__check_dimencions(other)
            return Matrix([[self[i, j] - other[i, j] for j in range(self.cols)] for i in range(self.rows)])
        else:
            self.__is_digit(other)
            return Matrix([[self[i, j] - other for j in range(self.cols)] for i in range(self.rows)])


my_matrix_1 = Matrix(4, 5, 0)
res = my_matrix_1[0, 0]
my_matrix_1[1, 2] = 5
my_matrix_2 = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
print(my_matrix_2[0, 0])
print(my_matrix_2[0, 1])
print(my_matrix_2[1, 2])
print(my_matrix_2[3, 4])
my_matrix_3 = my_matrix_1 + 10
my_matrix_4 = my_matrix_2 + my_matrix_3
my_matrix_5 = my_matrix_3 - my_matrix_1
my_matrix_6 = my_matrix_1 - 10
for my_matrix in my_matrix_1, my_matrix_2, my_matrix_3, my_matrix_4, my_matrix_5, my_matrix_6:
    for row in my_matrix.lst:
        for element in row:
            print(element, end=" ")
        print()
    print()
# print(my_matrix_2[4, 4])
# my_matrix_7 = Matrix("", 0, 0)
# my_matrix_6[2, 1] = ""
