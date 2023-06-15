# Declare in the program the class Player, the objects of which are created by the command:
#
# player = Player(name, old, score)
#
# where name - player name (string); old - player's age (integer); score - points scored in the game (integer).
# In each object of the Player class, similar local attributes should be created: name, old, score.
#
# The following function should work with objects of the Player class:
#
# bool(player)
#
# which returns True if the score is greater than zero and False otherwise.
#
# With the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# rows are read from the input stream into the list of lst_in strings. Each line is written in the format:
#
# 'Name; age; glasses'
#
# For example:
#
# Balakirev; 34; 2048
# Mediel; 27; 0
# Vlad; 18; 9012
# Nina P; 33; 0
#
# Each line of the lst_in list must be represented as an object of the Player class with the corresponding data.
# And form a list of players from these objects.
#
# Filter this list (create a new one: players_filtered) leaving all players with scores greater than zero.
# To do this, use the standard filter() function in conjunction with Python's bool() function.


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = [
    "Balakirev; 34; 2048",
    "Mediel; 27; 0",
    "Vlad; 18; 9012",
    "Nina P; 33; 0"
]

players = []

for string in lst_in:
    name, old, score = string.split(";")
    players.append(Player(name.strip(), int(old), int(score)))

players_filtered = list(filter(bool, players))
print(players_filtered)
