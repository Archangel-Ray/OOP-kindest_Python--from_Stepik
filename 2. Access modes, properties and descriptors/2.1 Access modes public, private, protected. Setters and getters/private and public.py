# Declare a class named Clock and define the following variables and methods in it:
#
# - private local variable time for storing the current time, an integer (its own for each object of the Clock class
# with an initial value of 0);
# - public method set_time(tm) for setting the current time (assigns the value tm to the private local property time
# if the check_time(tm) method returns True);
# - public method get_time() to get the current time from the private local variable time;
# - private class method check_time(tm) for checking the correctness of the time in the tm variable
# (returns True if the value is correct and False otherwise).
#
# Validation is performed according to the criterion: tm must be an integer,
# greater than or equal to zero and less than 100,000.
#
# Clock class objects are supposed to be used by the command:
#
# clock = Clock(time)
# Create a clock object of class Clock and set the time to 4530.


class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def __check_time(self, tm):
        return type(tm) == int and 0 <= tm < 100000


clock = Clock(4530)
