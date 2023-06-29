# With your work, you impressed the authorities a little and they instructed you to complete the listener pattern.
# The idea of ​​this pattern is very simple and the basis is implemented as follows:
#
# class observer:
#     def update(self, data):
#         pass
#
#     def __hash__(self):
#         return hash(id(self))
#
#
# class Subject:
#     def __init__(self):
#         self.__observers = {}
#         self.__data = None
#
#     def add_observer(self, observer):
#         self.__observers[observer] = observer
#
#     def remove_observer(self, observer):
#         if observer in self.__observers:
#             self.__observers.pop(observer)
#
#     def __notify_observer(self):
#         for ob in self.__observers:
#             ob.update(self.__data)
#
#     def change_data(self, data):
#         self.__data = data
#         self.__notify_observer()
#
# Here, in objects of the Subject class, you can register (add) a lot of objects of the Observer class (observer,
# listener). This is done using the add_observer() method. Then, when the data (self.__data) is changed by calling
# the change_data() method of the Subject class, the update() method is automatically called on all listeners.
# In this method, you can write a very different logic of work when changing data in each specific listener.
#
# In the project, this pattern is supposed to be used to display weather information in various formats:
#
# - current temperature;
# - current atmospheric pressure;
# - current air humidity.
#
# To do this, the data itself is defined by the class:
#
# classData:
#     def __init__(self, temp, press, wet):
#         self.temp = temp # temperature
#         self.press = press # pressure
#         self.wet = wet # moisture
#
# And you are instructed to develop child classes inherited from the Observer class, with names:
#
# TemperatureView - a listener for displaying temperature information;
# PressureView - listener for displaying pressure information;
# WetView is a listener for displaying moisture information.
#
# Each of these classes must override the update() method of the base class to output
# to the console information in the format:
#
# TemperatureView: 'Current temperature number'
# PressureView: 'Current pressure number'
# WetView: 'Current humidity number'
#
# Important: To print information to the console, use the print() function with one F-string argument.
#
# An example of using classes (you do not need to write these lines in the program):
#
# subject = Subject()
# tv = TemperatureView()
# pr = PressureView()
# wet = WetView()
#
# subject.add_observer(tv)
# subject.add_observer(pr)
# subject.add_observer(wet)
#
# subject.change_data(Data(23, 150, 83))
# # will output the lines:
# # Current temperature 23
# # Current pressure 150
# # Current humidity 83
# subject.remove_observer(wet)
# subject.change_data(Data(24, 148, 80))
# # will output the lines:
# # Current temperature 24
# # Current pressure 148


class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp
        self.press = press
        self.wet = wet


class TemperatureView(Observer):
    def update(self, data):
        if data:
            print(f"Current temperature {data.temp}")


class PressureView(Observer):
    def update(self, data):
        if data:
            print(f"Current pressure {data.press}")


class WetView(Observer):
    def update(self, data):
        if data:
            print(f"Current humidity {data.wet}")


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
print()
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))
