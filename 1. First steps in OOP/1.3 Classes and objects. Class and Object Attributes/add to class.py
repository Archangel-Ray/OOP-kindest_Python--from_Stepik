# Declare an empty class named Car. Use the setattr() function to add attributes to this class:
#
# model: 'Toyota'
# color: 'pink'
# number: 'P111YY77'
#
# Display the value of the color attribute using the __dict__ dictionary of the Car class.


class Car:
    pass


setattr(Car, 'model', "Toyota")
setattr(Car, 'color', "pink")
setattr(Car, 'number', "P111YY77")
print(Car.__dict__["color"])
