# Declare a function with signature:
#
# def input_int_numbers(): ...
#
# which would read a string of entered integers, separated by spaces,
# and return a tuple of entered numbers (as integers, not strings).
#
# If at least one value is not an integer, then throw an exception with the command:
#
# raise TypeError('all numbers must be integers')
#
# Call this function in a loop until the user has entered all the integer values ​​in the string
# (that is, the loop ends when the function has completed normally, without throwing an exception).
#
# Display the read values, written as a space-separated string.


def input_int_numbers():
    return tuple(map(int, input().split()))


result = ()
while not result:
    try:
        result = input_int_numbers()
    except:
        pass

print(*result)
