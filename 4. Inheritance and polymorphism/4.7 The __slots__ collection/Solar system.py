# Declare a class Planet, the objects of which are created by the command:
#
# p = Planet(name, diameter, period_solar, period)
#
# where name is the name of the planet; diameter - diameter of the planet (any positive number);
# period_solar - period (time) of the planet's revolution around the Sun (any positive number);
# period - period of rotation of the planet around its axis (any positive number).
#
# In each object of the Planet class, local attributes should be formed with the names: _name, _diameter, _period_solar,
# _period and corresponding values.
#
# Next, declare a class named SolarSystem (solar system). In objects of this class, the following local attributes
# must be allowed (the limit is set via the __slots__ collection):
#
# _mercury - reference to the planet Mercury (object of the Planet class);
# _venus - reference to the planet Venus (object of the Planet class);
# _earth - reference to the planet Earth (object of the Planet class);
# _mars - reference to the planet Mars (object of the Planet class);
# _jupiter - reference to the planet Jupiter (object of the Planet class);
# _saturn - reference to the planet Saturn (object of the Planet class);
# _uranus - reference to the planet Uranus (object of the Planet class);
# _neptune - reference to the planet Neptune (object of the Planet class).
#
# An object of the SolarSystem class must be created with the command:
#
# s_system = SolarSystem()
#
# and be only one (simultaneously in the program two or more objects of the SolarSystem class are unacceptable).
# Use the Singleton pattern for this.
#
# At the time of creation of the SolarSystem object, the listed local attributes should be automatically created
# and refer to the corresponding objects of the Planet class with the following planet data:
#
# Create an s_system object of the SolarSystem class in the program.


class Planet:
    def __init__(self, name, diameter, period_solar, period):
        self._name = name
        self._diameter = diameter
        self._period_solar = period_solar
        self._period = period


class SolarSystem:
    __object = None
    __slots__ = "_mercury", "_venus", "_earth", "_mars", "_jupiter", "_saturn", "_uranus", "_neptune"

    def __new__(cls, *args, **kwargs):
        if SolarSystem.__object is None:
            SolarSystem.__object = super().__new__(cls)
        return cls.__object

    def __del__(self):
        SolarSystem.__object = None

    def __init__(self):
        self._mercury = Planet(name="Mercury", diameter=4878, period_solar=87.97, period=1407.5)
        self._venus = Planet(name="Venus", diameter=12104, period_solar=224.7, period=5832.45)
        self._earth = Planet(name="Earth", diameter=12756, period_solar=365.3, period=23.93)
        self._mars = Planet(name="Mars", diameter=6794, period_solar=687, period=24.62)
        self._jupiter = Planet(name="Jupiter", diameter=142800, period_solar=4330, period=9.9)
        self._saturn = Planet(name="Saturn", diameter=120660, period_solar=10753, period=10.63)
        self._uranus = Planet(name="Uranus", diameter=51118, period_solar=30665, period=17.2)
        self._neptune = Planet(name="Neptune", diameter=49528, period_solar=60150, period=16.1)


s_system = SolarSystem()
print(
    [
        [getattr(s_system, attr)._name,
         getattr(s_system, attr)._diameter,
         getattr(s_system, attr)._period_solar,
         getattr(s_system, attr)._period]
        for attr in s_system.__slots__
    ]
)
