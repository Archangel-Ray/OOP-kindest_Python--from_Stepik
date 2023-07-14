# You have passed a series of trials and accomplished many feats in order to face a real challenge worthy of only
# the elite! To confirm your knowledge and skills, you are invited to take the stage of initiation
# into object-oriented programming. And here is the task that fell to your lot.
#
# The management of the company does not know what to do with itself all day long. Therefore,
# they decided to give their programmers the task of writing a program for the game 'Battleship'.
# But this game will be a little different from the classic. For those who are not familiar with this ancient,
# like the world, game, let me remind you of its brief description.
#
# Each player draws a playing field 10 x 10 cells on his paper and places ten ships on it: single-deck - 4;
# two-deck - 3; three-deck - 2; four-deck - 1.
#
# The ships are placed randomly, but in such a way that they do not go beyond the playing field and
# do not touch each other (including diagonally).
#
# Then, the players take turns calling the cells where the shots are fired. And they mark these shots
# on another similar field of 10 x 10 cells, which represents the opponent's field. At the same time,
# the opponent must honestly answer: 'miss' if not a single ship was hit and 'hit' if there was a hit.
# The player who first hits all the opponent's ships wins.
#
# But it was a game from the deep past. Now, in the computer age, ships on the playing field can move in the direction
# of their orientation by one cell after each move of the opponent, if they have not received a single hit.
#
# So, personally, you are instructed to make an important fragment of this game - the placement and control of ships
# in this game. And the task itself sounds like this.
#
# Technical task
#
# The program needs to declare two classes:
#
# Ship - to represent ships;
# GamePole - to describe the playing field.
# Ship class
#
# The Ship class must describe ships with the following set of parameters:
#
# x, y - coordinates of the beginning of the location of the ship (integer);
# length - ship length (number of decks: integer value: 1, 2, 3 or 4);
# tp - ship orientation (1 - horizontal; 2 - vertical).
#
# Ship class objects must be created with the commands:
#
# ship = Ship(length)
# ship = Ship(length, tp)
# ship = Ship(length, tp, x, y)
#
# By default (if not specified) tp = 1 and x, y coordinates are None.
#
# The following local attributes must be formed in each object of the Ship class:
#
# _x, _y - coordinates of the ship
#          (integer values ​​in the range [0; size), where size is the size of the playing field);
# _length - ship length (number of decks);
# _tp - ship orientation;
# _is_move - is it possible to move the ship (initially equals True);
# _cells - initially a list of length length, consisting of ones (for example, with length=3, _cells = [1, 1, 1]).
#
# The _cells list will signal when an opponent hits any deck of the ship. If the value is 1, then there was no hit,
# and if the value is 2, then the corresponding deck was hit.
#
# When it hits a ship (at least one of its decks), the _is_move flag is set to False and the ship's movement across
# the playing field stops.
#
# The following methods must be implemented in the Ship class itself
# (of course, other, additional methods are also possible):
#
# set_start_coords(x, y) - setting start coordinates (writing values ​​into local attributes _x, _y);
# get_start_coords() - getting the initial coordinates of the ship as a tuple x, y;
# move(go) - move the ship in the direction of its orientation to go cells
#            (go = 1 - move in one direction per cell; go = -1 - move in the other direction by one cell);
#            movement is possible only if the flag _is_move = True;
# is_collide(ship) - check for a collision with another ship (a collision is considered if another ship either
#            intersects with the current one or simply touches, including diagonally);
#            the method returns True if there is a collision and False otherwise;
# is_out_pole(size) - check if the ship is out of the playing field (size - size of the playing field, usually
#            size = 10); the boolean True is returned if the ship left the playing field and False otherwise;
#
# Use the __getitem__() and __setitem__() magic methods to access the _cells collection like this:
#
# value = ship[indx] # read value from _cells at index indx (index starts from 0)
# ship[indx] = value # write new value to _cells collection
#
# GamePole class
#
# The following GamePole class should provide work with the game field.
# Objects of this class are created by the command:
#
# pole = GamePole(size)
#
# where size is the dimensions of the playing field (usually, size = 10).
#
# Local attributes must be formed in each object of this class:
#
# _size - playing field size (positive integer);
# _ships - a list of ships (objects of the Ship class); initially empty list.
#
# The following methods must be implemented in the GamePole class itself (other additional methods are possible):
#
# init() - initial initialization of the playing field; here a list of ships (objects of the Ship class) is created:
# single-deck - 4; two-deck - 3; three-deck - 2; four-deck - 1 (the orientation of these ships must be random).
#
# Ships are formed in the _ships collection as follows: single-deck - 4; two-deck - 3; three-deck - 2; four-deck - 1.
# The orientation of these ships should be random. To do this, you can use the randint function as follows:
#
# [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
#
# The initial x, y coordinates of unplaced ships are None.
#
# After that, they are placed on the playing field with random coordinates
# so that the ships do not intersect with each other.
#
# get_ships() - returns a collection of _ships;
# move_ships() - moves each ship in the _ships collection one cell (randomly forward or backward) in the direction
#                of the ship's orientation; if moving to the selected side is impossible (another ship or the limits
#                of the playing field), then try to move to the opposite side,
#                otherwise (if movements are impossible), stay in place;
# show() - displaying the playing field in the console (ships should be displayed with values
#          ​​from the _cells collection of each ship, water - with the value 0);
#
# get_pole() - Get the current playing field as a two-dimensional (nested) tuple of size x size elements.
#
# An example of displaying the playing field:
#
# 0 0 1 0 1 1 1 0 0 0
# 1 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 1
# 0 0 0 0 1 0 1 0 0 1
# 0 0 0 0 0 0 1 0 0 0
# 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0 0 0
# 0 1 1 1 1 0 0 0 0 0
# 0 0 0 0 0 0 0 1 1 0
#
# An example of using classes (do not write these lines in the program):
#
# SIZE_GAME_POLE = 10
#
# pole = GamePole(SIZE_GAME_POLE)
# pole.init()
# pole.show()
#
# pole.move_ships()
# print()
# pole.show()
#
# The program only needs to declare the Ship and GamePole classes with the appropriate functionality.
# You don't need to display anything on the screen.
#
# P.S. For the most devoted fans of programming and OOP. Finish off this program by adding another SeaBattle class
# to handle the overall gameplay. The game must be played between a human and a computer. Shots from the computer
# can be implemented randomly in free cells. Play this game and win against the computer.
from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self.x = x
        self.y = y
        self._length = length
        self._tp = tp
        self._cells = [1 for _ in range(length)]
        self._is_move = True

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, value):
        self._tp = value

    @property
    def cells(self):
        return self._cells

    def get_start_coords(self):
        return self.x, self.y

    def set_start_coords(self, x, y):
        self.x = x
        self.y = y

    def move(self, go):
        if self._is_move:
            if self.tp == 1:
                self.x += go
            if self.tp == 2:
                self.y += go

    def ship_location(self):
        list_of_ship_location = []
        if self.tp == 1:
            for i in range(self._length):
                list_of_ship_location.append((self.x + i, self.y))
        if self.tp == 2:
            for i in range(self._length):
                list_of_ship_location.append((self.x, self.y + i))
        return list_of_ship_location

    def surrounding(self):
        surround = set()
        for coords in self.ship_location():
            list_of_cells_around = [
                (coords[0] - 1, coords[1] - 1), (coords[0] - 1, coords[1]), (coords[0] - 1, coords[1] + 1),
                (coords[0], coords[1] - 1), (coords[0], coords[1]), (coords[0], coords[1] + 1),
                (coords[0] + 1, coords[1] - 1), (coords[0] + 1, coords[1]), (coords[0] + 1, coords[1] + 1)
            ]
            for cell in list_of_cells_around:
                surround.add(cell)
        return surround

    def is_collide(self, ship):
        return True if self.surrounding() & set(ship.ship_location()) else False

    def is_out_pole(self, size):
        for x, y in self.ship_location():
            if x < 0 or x >= size or y < 0 or y >= size:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value
        self._is_move = True if sum(self.cells) == self._length else False


class GamePole:
    def __init__(self, size=10):
        self.size = size
        self._ships = []
        self._pole = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def ships(self):
        return self._ships

    def add_ship(self, ship):
        self._ships.append(ship)

    def seize_ship(self):
        return self.ships.pop()

    def create_a_ship(self, length):
        return Ship(length, randint(1, 2), randint(0, self.size - length), randint(0, self.size - length))

    def collision(self, ship):
        if not ship.is_out_pole(self.size):
            collision = False
            for another in self._ships:
                if ship.is_collide(another):
                    collision = True
            if collision:
                return False
            else:
                return True
        return False

    def init(self):
        while True:
            new_ship = self.create_a_ship(4)
            if self.collision(new_ship):
                self.add_ship(new_ship)
                break
            else:
                continue

        for _ in range(2):
            while True:
                new_ship = self.create_a_ship(3)
                if self.collision(new_ship):
                    self.add_ship(new_ship)
                    break
                else:
                    continue
        for _ in range(3):
            while True:
                new_ship = self.create_a_ship(2)
                if self.collision(new_ship):
                    self.add_ship(new_ship)
                    break
                else:
                    continue
        for _ in range(4):
            while True:
                new_ship = self.create_a_ship(1)
                if self.collision(new_ship):
                    self.add_ship(new_ship)
                    break
                else:
                    continue

    def put_the_ship_on_the_field(self, ship):
        ship_deck_index = 0
        for coord_x, coord_y in ship.ship_location():
            self._pole[coord_y][coord_x] = ship.cells[ship_deck_index]
            ship_deck_index += 1

    def get_ships(self):
        return self._ships

    def move_ships(self):
        copy_list_ships = self.ships[:]
        while copy_list_ships:
            new_boat = copy_list_ships.pop()
            self.ships.remove(new_boat)
            new_boat.move(1)
            if self.collision(new_boat):
                self.add_ship(new_boat)
                continue
            new_boat.move(-2)
            if self.collision(new_boat):
                self.add_ship(new_boat)
                continue
            new_boat.move(1)
            self.add_ship(new_boat)

    def get_pole(self):
        self._pole = [["~" for _ in range(self.size)] for _ in range(self.size)]
        for next_ship in self._ships:
            self.put_the_ship_on_the_field(next_ship)
        return tuple(tuple(lst) for lst in self._pole)

    def show(self):
        for line in self.get_pole():
            print(*line)


pole = GamePole()
pole.init()
pole.show()
print()
pole.move_ships()
pole.show()
print()

ship_1 = Ship(2)
ship_2 = Ship(2, 1)
ship_3 = Ship(3, 2, 0, 0)

assert ship_3._length == 3 and ship_3._tp == 2 and ship_3._x == 0 and ship_3._y == 0, \
    "invalid values ​​of attributes of an object of class Ship"
assert ship_3._cells == [1, 1, 1], "invalid list of _cells"
assert ship_3._is_move, "invalid _is_move attribute value"

ship_3.set_start_coords(1, 2)
assert ship_3._x == 1 and ship_3._y == 2, "the set_start_coords() method worked incorrectly"
assert ship_3.get_start_coords() == (1, 2), "get_start_coords() method failed incorrectly"

ship_3.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "is_collide() method works incorrectly for Ship(4, 1, 0, 0) and Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "is_collide() method works incorrectly for Ship(4, 1, 0, 0) and Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "is_collide() method works incorrectly for Ship(4, 1, 0, 0) and Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "is_out_pole() method works incorrectly for Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "is_out_pole(10) method works incorrectly for Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "ship[indx] not working properly"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "ships go out of bounds"

        for ship_3 in p.get_ships():
            if s != ship_3:
                assert s.is_collide(ship_3) == False, "ships on the playing field are in contact"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "the get_pole method must return a two-dimensional tuple"
assert len(gp) == 10 and len(gp[0]) == 10, "invalid dimensions of the game field returned by the get_pole method"

pole_size_8 = GamePole(8)
pole_size_8.init()
