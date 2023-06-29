# It is necessary to declare a class_log decorator function for the class, which would create logging of class method
# calls. For example, the following lines of the program:
#
# vector_log = []
#
#
# class_log(vector_log)
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
# decorate the Vector class and add the names of the methods that were called when using this class to the vector_log
# list. In particular, after executing the commands:
#
# v = Vector(1, 2, 3)
# v[0] = 10
#
# there should be two methods in the vector_log list:
#
# ['__init__', '__setitem__']
#
# Your task is to implement a decorator named class_log.
#
# Reminder. Previously, you have already created a decorator function for the class like this:
#
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
# Use this principle to successfully complete the feat.


def class_log(log_lst):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_methods_decorator(v))

        return cls

    def log_methods_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return log_methods


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)
