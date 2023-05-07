# Declare two classes:
#
# Cell - to represent the playing field cell;
# GamePole - to control the playing field, size N x N cells.
#
# Using the Cell class, it is supposed to create individual cells with the command:
#
# c1 = Cell(around_mines, mine)
#
# Here around_mines is the number of mines around the given cell of the field; mine - boolean value (True/False)
# indicating the presence of a mine in the current cell. At the same time, local properties must be created
# in each object of the Cell class:
#
# around_mines - number of mines around the cell (initial value 0);
# mine - the presence of a mine in the current cell (True/False);
# fl_open - opened/closed cell - boolean value (True/False). Initially, all cells are closed (False).
#
# Using the GamePole class, it should be possible to create a square playing field with N x N cells:
#
# pole_game = GamePole(N, M)
#
# Here N is the size of the field; M - the total number of mines on the field. In this case, each cell is represented
# by an object of the Cell class and all objects are stored in a two-dimensional list of N x N elements - a local
# property pole of the object of the GamePole class.
#
# The following methods must also be implemented in the GamePole class:
#
# init() - initialization of the field with a new arrangement of M mines (randomly on the playing field, of course,
# each mine must be in a separate cell).
# show() - displaying the field in the console as a table of the number of open cells (if the cell is not open,
# the # symbol is displayed).
#
# When creating an instance of the GamePole class in its initializer, the init() method should be called to initially
# initialize the game field.
#
# There may be other helper methods in the GamePole class.
#
# Create a pole_game instance of the GamePole class with field size N = 10 and number of mines M = 12.

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.size = N
        self.number_of_m = M
        self.pole = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.init()

    def init(self):
        all_mines = 0
        while all_mines < self.number_of_m:
            coordinate_x = randint(0, self.size - 1)
            coordinate_y = randint(0, self.size - 1)
            if self.pole[coordinate_x][coordinate_y].mine:
                continue
            self.pole[coordinate_x][coordinate_y].mine = True
            all_mines += 1

        around = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.size):
            for y in range(self.size):
                if not self.pole[x][y].mine:
                    mines = sum(self.pole[x+i][y+j].mine for i, j in around
                                if 0 <= x+i < self.size and 0 <= y+j < self.size)
                    self.pole[x][y].around_mines = mines

    def show(self):
        for cell in self.pole:
            print(*map(lambda c: '#' if not c.fl_open else c.around_mines if not c.mine else '*', cell))


pole_game = GamePole(10, 12)
pole_game.show()
