# It is necessary to declare the class Body (body), the objects of which are created by the command:
#
# body = Body(name, ro, volume)
#
# where name - body name (string); ro - body density (number: real or integer);
# volume - volume of the body (number: real or integer).
#
# Comparison operators must be implemented for objects of class Body:
#
# body1 > body2 # True if body1's weight is greater than body2's weight
# body1 == body2 # True if body1's weight is equal to body2's weight
# body1 < 10 # True if body1's weight is less than 10
# body2 == 5 # True if body2's weight is 5
#
# Body weight is calculated by the formula:
#
# m = ro * volume


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.body_mass = self.ro * self.volume

    def __gt__(self, other):
        if type(other) == Body:
            return self.body_mass > other.body_mass
        if type(other) in (int, float):
            return self.body_mass > other

    def __lt__(self, other):
        if type(other) == Body:
            return self.body_mass < other.body_mass
        if type(other) in (int, float):
            return self.body_mass < other


    def __eq__(self, other):
        if type(other) == Body:
            return self.body_mass == other.body_mass
        if type(other) in (int, float):
            return self.body_mass == other


body1 = Body("", 2, 2.5)
body2 = Body("", 2.5, 2)
print(body1 > body2)
print(body1 == body2)
print(body1 < 10)
print(body2 == 5)
