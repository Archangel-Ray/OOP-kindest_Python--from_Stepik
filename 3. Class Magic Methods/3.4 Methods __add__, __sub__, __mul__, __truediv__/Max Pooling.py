# In neural networks I use an operation called Max Pooling. Its essence is to scan a rectangular table of numbers
# (matrix) with a window of a certain size (usually 2x2 elements) and select the largest value within this window:
#
# Or, if the windows go beyond the matrix, then they are skipped (ignored):
#
# We will repeat this procedure. To do this, the program needs to declare a class named MaxPooling,
# whose objects are created by the command:
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
#
# where step - window shift step horizontally and vertically; size - window size horizontally and vertically.
#
# The default step and size parameters should take a tuple with values ​​(2, 2).
#
# To perform the Max Pooling operation, use the command:
#
# res = mp(matrix)
#
# where matrix is ​​a rectangular table of numbers; res - link to the result of processing the matrix table
# (a new table of numbers should be created).
#
# A rectangular table of numbers should be described by nested lists. If, when scanning a table, a part of the window
# goes beyond its limits, then discard this data (do not take into account the entire window).
#
# If matrix is ​​not a rectangular table or contains at least one non-numeric value, then an exception should be thrown
# with the command:
#
# raise ValueError('Invalid format for first parameter matrix.')
#
# An example of using the class (you do not need to write these lines in the program):
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]) # [[6 , 8], [9, 7]]
#
# The result will be a table of numbers:
#
# 6 8
# 9 7


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]
        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError("Invalid format for first parameter matrix.")
        h, w = self.size[0], self.size[1]
        sh, sw = self.step[0], self.step[1]
        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1
        new_matrix = [[0] * cols_range for _ in range(rows_range)]
        for ind_row in range(rows_range):
            for ind_col in range(cols_range):
                window_matrix = (x for r in matrix[ind_row * sh: ind_row * sh + h]
                                 for x in r[ind_col * sw: ind_col * sw + w])
                new_matrix[ind_row][ind_col] = max(window_matrix)
        return new_matrix


mp = MaxPooling()
small_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [9, 8, 7, 6]]
res = mp(small_matrix)
print(res)
