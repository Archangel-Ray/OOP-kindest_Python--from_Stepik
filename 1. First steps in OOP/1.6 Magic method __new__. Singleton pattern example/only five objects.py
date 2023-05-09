# Declare a SingletonFive class that can be used to create objects with the command:
#
# a = SingletonFive( name )
#
# Here, the name is the data that is stored in the local name property of the created object.
#
# This class should only form the first five objects. The rest (sixth, seventh, etc.) should be a reference
# to the last (fifth) created object.
#
# Create the first ten objects of the SingletonFive class with the following code snippet:
#
# objs = [SingletonFive(str(n)) for n in range(10)]


class SingletonFive:
    __obj = None
    __counter = 0

    def __new__(cls, *args, **kwargs):
        if cls.__counter < 5:
            cls.__obj = super().__new__(cls)
            cls.__counter += 1

        return cls.__obj

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for object_in in objs:
    print(object_in.__dict__)
