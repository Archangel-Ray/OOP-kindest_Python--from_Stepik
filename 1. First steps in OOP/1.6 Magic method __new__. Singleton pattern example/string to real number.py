# The program is supposed to implement a string parser (processor) into a certain output format.
# The following class is declared for this:
#
# class loader:
#   def parse_format(self, string, factory):
#       seq = factory.build_sequence()
#       for sub in string.split(','):
#           item = factory.build_number(sub)
#           seq append(item)
#
#       return seq
#
# And it is supposed to be used like this:
#
# ld = Loader()
# res = ld.parse_format('4, 5, -6.5', Factory())
#
# The output (in the res variable) is expected to be a list of a set of real numbers.
# For example, for a given string, you should get:
#
# [4.0, 5.0, -6.5]
#
# To implement this idea, it is necessary to write the Factory class with two methods at the beginning of the program:
#
# build_sequence(self) - to create an initial empty list (the method must return an empty list);
# build_number(self, string) - to convert the string (string) passed to the method into a real value
# (the method must return the received real number).
#
# Declare a class named Factory to get the output you're looking for.


class Factory:
    def build_sequence(self):
        return []

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print(res)
