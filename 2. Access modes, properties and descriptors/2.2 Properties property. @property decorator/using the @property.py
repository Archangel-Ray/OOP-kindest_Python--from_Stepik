# Declare a class Car in the program, in which implement a property object named model to write and read information
# about the car model from the local private variable __model.
#
# Declare the property object with the @property decorator.
# Also, checks must be implemented in the model property object:
#
# - car model is a string;
# - the length of the model string must be in the range [2; 100].
#
# If the check fails, then the local __model property remains unchanged.
#
# Objects of class Car are supposed to be created by the command:
#
# car = Car()
#
# and then work with the object-property, for example:
#
# car.model = "Toyota"


class Car:
    def __init__(self):
        self.__model = ""

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) is str:
            if 2 < len(model) < 100:
                self.__model = model


car = Car()
car.model = "Toyota"
print(car.model, car.__dict__)
car.model = "T"
print(car.model, car.__dict__)
car.model = "The coolest car in the world is the flying saucer. " \
            "if you don't believe me, then sit in a UFO and check it out. " \
            "unless of course you can find it in our jungle."
print(car.model, car.__dict__)
car.model = 123
print(car.model, car.__dict__)
car.model = "Volga"
print(car.model, car.__dict__)
