# The program declares the integer_params function for the Vector class, which applies the
# integer_params_decorated decorator to each class method:
#
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
# @integer_params
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#     def set_coords(self, *coords, reverse=False):
#         c = list(coords)
#         self.__coords = c if not reverse else c[::-1]
#
# The integer_params_decorated decorator must check that all arguments passed to class methods (except the first self)
# are integers (of type int). If this is not the case, then an exception should be thrown with the command:
#
# raise TypeError('arguments must be integers')
#
# Your task is to declare this decorator function.
#
# An example of using the class (do not write these lines in the program):
#
# vector = Vector(1, 2)
# print(vector[1])
# vector[1] = 20.4 # TypeError


def integer_params_decorated(func):
    def wrapper(self, *args, **kwargs):
        if not all(type(x) == int for x in args):
            raise TypeError("arguments must be integers")
        if not all(type(x) == int for x in kwargs.values()):
            raise TypeError("arguments must be integers")
        return func(self, *args, **kwargs)
    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)
print(vector.__dict__)
