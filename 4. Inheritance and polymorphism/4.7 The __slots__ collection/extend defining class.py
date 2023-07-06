# The base class Function (function) is declared in the program as follows:
#
# class Function:
#     def __init__(self):
#         self._amplitude = 1.0 # function amplitude
#         self._bias = 0.0 # function offset along the Oy axis
#
#     def __call__(self, x, *args, **kwargs):
#         return self._amplitude * self._get_function(x) + self._bias
#
#     def _get_function(self, x):
#         raise NotImplementedError('method _get_function must be overridden in a child class')
#
#     def __add__(self, other):
#         if type(other) not in (int, float):
#             raise TypeError('offset must be a number')
#
#         obj = self.__class__(self)
#         obj._bias = self._bias + other
#         return obj
#
# Here, two local attributes are created in the initializer:
#
# _amplitude - function amplitude;
# _bias - function offset along the y-axis (Oy).
#
# Next, in the __call__() method, the value of the function at point x is taken through the _get_function() method,
# which must be defined in child classes, multiplied by the amplitude of the function, and its offset is added.
# The following __add__() method allows you to change the bias of a function by changing the _bias attribute
# to the specified value of other.
#
# Please note that in the __add__() method, a new object is created by the command:
#
# obj = self.__class__(self)
#
# Here __class__ is a reference to the class to which the object self belongs. Thanks to this, objects
# of the corresponding child classes can be created in the base class. When an object is created, the self parameter
# is passed to it as an argument. This will create a copy of the object, that is, a new object with the same set
# and values ​​of local attributes.
#
# To provide this functionality, declare a child class named Linear (linear function y = k*x + b)
# whose objects are to be created with commands:
#
# obj = Linear(k, b)
# linear = Linear(obj) # this option is used in the base class in the __add__() method
#
# In the first case, a linear function object is created with parameters k and b. In the second,
# the creation of an object with the values ​​of the parameters k and b taken from the object obj.
#
# In each object of the class Linear, local attributes named _k and _b must be created with the corresponding values.
# As a result, a universal base class Function will be created for working with arbitrary functions from
# a single argument.
#
# You can use these classes as follows (you do not need to write these lines in the program):
#
# f = Linear(1, 0.5)
# f2 = f + 10 # offset change (_bias attribute)
# y1 = f(0) # 0.5
# y2 = f2(0) # 10.5
#
# Write another magic method in the base Function class to change the scale (amplitude)
# of the function so that the multiplication operator is available:
#
# f = Linear(1, 0.5)
# f2 = f * 5 # amplitude change (_amplitude attribute)
# y1 = f(0) # 0.5
# y2 = f2(0) # 2.5


class Function:
    def __init__(self):
        self._amplitude = 1.0
        self._bias = 0.0

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError("the _get_function method must be overridden in a subclass")

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError("offset must be a number")

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError("amplitude must be a number")

        obj = self.__class__(self)
        obj._amplitude *= other
        return obj


class Linear(Function):
    def __init__(self, k=None, b=None):
        super().__init__()
        if type(k) == Linear:
            self._k, self._b = k._k, k._b
        else:
            self._k = k
            self._b = b

    def _get_function(self, x):
        return self._k * x + self._b


f = Linear(1, 0.5)
f2 = f + 10  # offset change (_bias attribute)
y1 = f(0)  # 0.5
y2 = f2(0)  # 10.5

f2 = f * 5  # amplitude change (_amplitude attribute)
y11 = f(0)  # 0.5
y22 = f2(0)  # 2.5
print(y11, y22)
