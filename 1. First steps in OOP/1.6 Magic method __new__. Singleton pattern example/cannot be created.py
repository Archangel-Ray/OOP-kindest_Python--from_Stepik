# Declare a class AbstractClass whose objects could not be instantiated. When running the command:
#
# obj = AbstractClass()
# the obj variable must refer to a string with the content:
#
# Error: Can't create objects of abstract class


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Error: Can't create objects of abstract class"


AC = AbstractClass()
print(AC)
