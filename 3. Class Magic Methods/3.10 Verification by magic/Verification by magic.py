# You have passed the magical methods. The authorities appreciated your stamina, zeal and decided to give you a test
# to confirm the level of the acquired skills. You have the great honor of creating a complete Tic-Tac-Toe program.
# And here is the text with the task of the test itself.
#
# Technical task
#
# You need to declare a class named TicTacToe (tic-tac-toe) to control the gameplay.
# Objects of this class will be created by the command:
#
# game = TicTacToe()
#
# Each object of this class must have a public attribute:
#
# pole is a two-dimensional 3x3 tuple.
#
# Each element of the pole tuple is an object of the Cell class:
#
# cell = Cell()
#
# In objects of this class, a local property should be automatically formed:
#
# value - the current value in the cell: 0 - the cell is free; 1 - there is a cross; 2 - worth a zero.
#
# Also, with objects of the Cell class, the following function must be performed:
#
# bool(cell) - returns True if the cell is free (value = 0) and False otherwise.
#
# Each cell of the playing field must be accessed through the operators:
#
# res = game[i, j] # get value from cell with indices i, j
# game[i, j] = value # write a new value to the cell with indices i, j
#
# If the indices are incorrect (not integers or numbers outside the range [0; 2]),
# then an exception should be thrown with the command:
#
# raise IndexError('invalid indexes')
#
# In order not to operate with values ​​in the program: 0 - free cell; 1 - crosses and 2 - zeroes,
# the TicTacToe class must have three public attributes (class attributes):
#
# FREE_CELL = 0 # free cell
# HUMAN_X = 1 # cross (player - human)
# COMPUTER_O = 2 # zero (player - computer)
#
# The following methods must be declared in the TicTacToe class itself (at a minimum):
#
# init() - game initialization (clearing the playing field, possibly some other actions);
# show() - displaying the current state of the playing field (how exactly - at your discretion);
# human_go() - implementation of the player's move (requests the coordinates of a free cell and puts a cross there);
# computer_go() - implementation of the computer's move (randomly puts a zero in a free cell).
#
# Also, the TicTacToe class must contain the following property objects:
#
# is_human_win - returns True if a human won, False otherwise;
# is_computer_win - returns True if the computer won, False otherwise;
# is_draw - Returns True if draw, False otherwise.
#
# Finally, with objects of the TicTacToe class, the following function must be performed:
#
# bool(game) - returns True if the game is not over (no one has won and there are free cells) and False otherwise.
#
# All these functions and properties are supposed to be used as follows (do not write these lines in the program):
#
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
#
# game.show()
#
# if game.is_human_win:
#     print("Congratulations! You won!")
# elif game.is_computer_win:
#     print("Everything will work out in time")
# else:
#     print("dead heat")
#
# You only need to declare two classes in your program: TicTacToe and Cell, so that they can be used to play
# Tic-Tac-Toe between a human and a computer.
#
# P.S. There is no need to start the game and display anything on the screen. Just declare classes.
#
# P.S.S. Homework: Complete the creation of this game and beat the computer at least once.
from random import randint


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return self.value == 0


class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self._size = 3
        self._win = 0
        self.pole = tuple(tuple(Cell() for _ in range(self._size)) for _ in range(self._size))

    def __check_index(self, numerical):
        if type(numerical) not in (tuple, list) or len(numerical) != 2:
            raise IndexError("incorrectly specified indexes")
        if not (0 <= numerical[0] < self._size) or not (0 <= numerical[1] < self._size):
            raise IndexError("incorrectly specified indexes")

    def __update_win_status(self):
        for row in self.pole:
            if all(x.value == self.HUMAN_X for x in row):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in row):
                self._win = 2
                return
        for i in range(self._size):
            if all(x.value == self.HUMAN_X for x in (row[i] for row in self.pole)):
                self._win = 1
                return
            if all(x.value == self.COMPUTER_O for x in (row[i] for row in self.pole)):
                self._win = 2
                return
        if all(self.pole[i][i].value == self.HUMAN_X for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.HUMAN_X for i in range(self._size)):
            self._win = 1
            return
        if all(self.pole[i][i].value == self.COMPUTER_O for i in range(self._size)) or \
                all(self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(self._size)):
            self._win = 2
            return
        if all(x.value != self.FREE_CELL for row in self.pole for x in row):
            self._win = 3

    def __getitem__(self, item):
        self.__check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.pole[key[0]][key[1]].value = value
        self.__update_win_status()

    def init(self):
        for row in self.pole:
            for obj in row:
                obj.value = 0
        self._win = 0

    def show(self):
        print(" | 0 1 2")
        print("-| - - -")
        for i, row in enumerate(self.pole):
            print(i, "|", sep="", end=" ")
            for obj in row:
                if obj.value == 0:
                    print(" ", end=" ")
                if obj.value == 1:
                    print("X", end=" ")
                if obj.value == 2:
                    print("O", end=" ")
            print()
        print()

    def human_go(self):
        if not self:
            return
        while True:
            x, y = map(int, input("enter cell coordinates: ").split())
            if not (0 <= x < self._size) or not (0 <= y < self._size):
                continue
            if self.pole[x][y].value == self.FREE_CELL:
                self[x, y] = self.HUMAN_X
                break

    def computer_go(self):
        if not self:
            return
        while True:
            coord_x, coord_y = (randint(0, self._size - 1), randint(0, self._size - 1))
            if self[coord_x, coord_y] == self.FREE_CELL:
                self[coord_x, coord_y] = self.COMPUTER_O
                break

    @property
    def is_human_win(self):
        return self._win == 1

    @property
    def is_computer_win(self):
        return self._win == 2

    @property
    def is_draw(self):
        return self._win == 3

    def __bool__(self):
        return self._win == 0 and self._win not in (1, 2, 3)


game = TicTacToe()
game[0, 1] = 1
cell_1 = game[2, 2]
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Congratulations! You won!")
elif game.is_computer_win:
    print("Everything will work out in time")
else:
    print("dead heat")
