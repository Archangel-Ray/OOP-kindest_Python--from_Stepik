# Declare the InputValues ​​decorator class with the render parameter, which is a function or object for converting data
# from strings to another data type. To implement such a decorator, the render parameter must be specified
# in the __init__() initializer, and the __call__() magic method is defined as a decorator function:
#
# class InputValues:
#   def __init__(self, render): # render is a reference to a function or object to convert
#       # program lines here
#
#   def __call__(self, func): # func is a reference to the function being decorated
#       def wrapper(*args, **kwargs):
#           # program lines here
#       return wrapper
#
# As a renderer, declare a class named RenderDigit that would convert string data to integers.
# Objects of this class are created by the command:
#
# render = RenderDigit()
#
# and apply as follows:
#
# d1 = render('123') # 123 (integer)
# d2 = render('45.54') # None (not an integer)
# d3 = render('-56') # -56 (integer)
# d4 = render('12fg') # None (not an integer)
# d5 = render('abc') # None (not an integer)
#
# Decorate the standard input function with the InputValues ​​decorator and the render object of the RenderDigit class
# so that when you enter space-separated integers, a list of the entered values ​​is returned at the output.
# And in place of non-integer data - the value None.
#
# For example, when entering the string:
#
# '1 -5.3 0.34 abc 45f -5'
#
# should return a list:
#
# [1, None, None, None, None, -5]
#
# Name the decorated function input_dg and call it with the command:
#
# res = input_dg()
#
# Print the result of res to the screen.


class RenderDigit:
    def __call__(self, string):
        try:
            return int(string)
        except:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*string):
            return list(map(self.render, func(*string).split()))
        return wrapper


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
