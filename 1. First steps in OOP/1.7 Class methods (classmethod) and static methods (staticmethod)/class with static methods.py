# The program is supposed to implement a parser (processor) of a string with string data into a certain output format.
# The following class is declared for this:
#
# class loader:
#   @staticmethod
#       def parse_format(string, factory):
#           seq = factory.build_sequence()
#           for sub in string.split(','):
#               item = factory.build_number(sub)
#               seq append(item)
#
#           return seq
#
# And it is supposed to be used like this:
#
# res = Loader.parse_format('4, 5, -6', Factory)
#
# The output (in the res variable) is expected to be a list of a set of integers.
# For example, for a given string, you should get:
#
# [4, 5, -6]
#
# To implement this idea, it is necessary to write the Factory class with two static methods at the beginning
# of the program:
#
# build_sequence() - to create an empty list (the method returns an empty list);
# build_number(string) - to convert a string (string) into an integer (the method returns the resulting integer value).
#
# Declare a class named Factory to get the output you're looking for.


class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
print(res)
