# In programming practice, the else block is used as an element of program debugging: the text of the program
# is written into it, in which exceptions that are caught in the try block will certainly not occur.
# Let's put this example into practice.
#
# You need to declare a function with signature:
#
# def get_loss(w1, w2, w3, w4): ...
#
# where w1, w2, w3, w4 are any numbers. The function must return the value calculated by the formula:
#
# y = 10 * w1 // w2 - 5 * w2 * w3 + w4
#
# Here, the calculation fragment w1 // w2 contains a potential divide-by-zero error,
# so it should be done in a try block. And in the else block,
# continue the calculations where division operations are not used.
#
# If division by zero occurs, then the function should return a string:
#
# 'division by zero'


def get_loss(w1, w2, w3, w4):
    try:
        y = 10 * w1 // w2 - 5 * w2 * w3 + w4
        return y
    except ZeroDivisionError:
        return "division by zero"


value_1 = get_loss(100, 2, 3, 4)
value_2 = get_loss(2, 0, 3, 5)
print(value_1, value_2, sep="\n")
