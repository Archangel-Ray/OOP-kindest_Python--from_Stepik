# Declare the InputDigits decorator class to decorate the standard input function so that when you enter a string
# of integers separated by a space, for example:
#
# '12 -5 10 83'
#
# the output was a list of integers:
#
# [12, -5, 10, 83]
#
# Name the decorated function input_dg and call it with the command:
#
# res = input_dg()


class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        return list(map(int, self.func().split()))


input_dg = InputDigits(input)
res = input_dg()
print(res)
