# Declare a DeltaClock class to calculate the time difference. Objects of this class must be created with the command:
#
# dt = DeltaClock(clock1, clock2)
# where clock1, clock2 are objects of another Clock class to store the current time.
# These objects must be created with the command:
#
# clock = Clock(hours, minutes, seconds)
#
# where hours, minutes, seconds - hours, minutes, seconds (non-negative integers).
#
# The Clock class must also have (at least) one method (others are possible):
#
# get_time() - Returns the current time in seconds (i.e. hours * 3600 + minutes * 60 + seconds).
#
# After creating the dt object of the DeltaClock class, the following commands should be executed with it:
#
# str_dt = str(dt) # returns the time difference string clock1 - clock2 in the format hours: minutes: seconds
# len_dt = len(dt) # time difference between clock1 and clock2 in seconds (integer)
# print(dt) # displays the time difference string clock1 - clock2 in the format: hours: minutes: seconds
#
# If the difference is negative, then the time difference is considered zero.
#
# An example of using classes (you do not need to write these lines in the program):
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt)#01:30:00
# len_dt = len(dt) # 5400
#
# Note that a non-significant zero is added if the number is less than 10.


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        if len(self):
            return f"{self.clock1.hours - self.clock2.hours:02}: " \
                f"{self.clock1.minutes - self.clock2.minutes:02}: " \
                f"{self.clock1.seconds - self.clock2.seconds:02}"
        else:
            return "00: 00: 00"

    def __len__(self):
        difference = self.clock1.get_time() - self.clock2.get_time()
        return difference if difference > 0 else 0


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)
print(len(dt))
