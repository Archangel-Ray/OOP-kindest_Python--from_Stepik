# With the help of inheritance, it is possible to 'fill' the child classes with the necessary qualities (properties).
# As an example, declare a class in your program with the name:
#
# Singleton
#
# which would allow only one instance to be created (all subsequent instances must refer to the first one).
# How to do this, you should already know from this course.
#
# Then, declare another class named:
#
# Game
#
# which would be inherited from the Singleton class. Objects of the Game class must be created with the command:
#
# game = game(name)
#
# where name is the name of the game (string).
# Each object of the Game class must create a name attribute with the appropriate content.
#
# Make sure the name attribute is set to the value of the first object created
# (if it isn't, adjust the child class's initializer to make this condition true).


class Singleton:
    _instance = None
    _instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls._instance_base is None:
                cls._instance_base = object.__new__(cls)
            return cls._instance_base

        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name):
        if "name" not in self.__dict__:
            self.name = name


singl = Singleton()
game_1 = Game("game - 1")
game_2 = Game("game - 2")
print(game_2.__dict__.values())
