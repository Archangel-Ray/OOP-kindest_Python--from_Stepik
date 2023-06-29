# Declare the base class Aircraft (aircraft), whose objects are created by the command:
#
# air = Aircraft(model, mass, speed, top)
#
# where model - aircraft model (string); mass - lifting weight of the aircraft (any positive number);
# speed - maximum speed (any positive number); top - maximum flight height (any positive number).
#
# In each object of the Aircraft class, local attributes must be created with the names:
# _model, _mass, _speed, _top and the corresponding values. If the passed arguments do not match
# the specified criteria (string, any positive number), then an exception is generated by the command:
#
# raise TypeError('wrong argument type')
#
# Next, in the program, declare the following child classes:
#
# Passenger Aircraft - passenger aircraft;
# WarPlane - military aircraft.
#
# Objects of these classes are created by the commands:
#
# pa = PassengerAircraft(model, mass, speed, top, chairs) # chairs - number of passenger seats (positive integer)
# wp = WarPlane(model, mass, speed, top, weapons) # weapons - weapons (dictionary);
# keys - the name of the weapon, the value - the number
#
# In each object of the PassengerAircraft and WarPlane classes, local attributes with the names _chairs and _weapons,
# respectively, must be formed. The rest of the attributes must be initialized through the base class initializer.
#
# In the initializers of the PassengerAircraft and WarPlane classes, check the correctness of the passed chairs and
# weapons arguments. If the data type does not match, then throw an exception with the command:
#
# raise TypeError('wrong argument type')
#
# Create four aircraft objects in the program with the following data:
#
# PassengerAircraft: MS-21, 1250, 8000, 12000.5, 140
# Passenger Aircraft: SuperJet, 1145, 8640, 11034, 80
# WarPlane: MiG-35, 7034, 25000, 2000, {'rocket': 4, 'bomb': 10}
# WarPlane: Su-35, 7034, 34000, 2400, {'rocket': 4, 'bomb': 7}
#
# All these objects are represented as a list of planes.


class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.model = model
        self.mass = mass
        self.speed = speed
        self.top = top

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if type(value) != str:
            raise TypeError("invalid argument type")
        self._model = value

    @staticmethod
    def __check_int(value):
        if type(value) not in (int, float) or value <= 0:
            raise TypeError("invalid argument type")

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self.__check_int(value)
        self._mass = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self.__check_int(value)
        self._speed = value

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self.__check_int(value)
        self._top = value


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.chairs = chairs

    @property
    def chairs(self):
        return self._chairs

    @chairs.setter
    def chairs(self, value):
        if type(value) != int:
            raise TypeError("invalid argument type")
        self._chairs = value


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.weapons = weapons

    @property
    def weapons(self):
        return self._weapons

    @weapons.setter
    def weapons(self, value):
        if type(value) != dict or \
                {type(x) for x in value.keys()} != {str} or \
                {True if type(x) not in (int, float) else False for x in value.values()} != {False}:
            raise TypeError("invalid argument type")
        self._weapons = value


planes = [PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
          PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
          WarPlane("Миг-35", 7034, 25000, 2000, {"missile": 4, "bomb": 10.3}),
          WarPlane("Су-35", 7034, 34000, 2400, {"missile": 4, "bomb": 7})]
print(planes)