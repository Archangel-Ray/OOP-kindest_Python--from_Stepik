# The program enters two values ​​in one line separated by a space. Values ​​can be numbers, words, boolean values
# ​​(True/False). You need to read these values ​​from the input stream. If both values ​​are numbers, then calculate
# their sum, otherwise combine them into one string using the + operator (string concatenation).
# Display the result on the screen (in the finally block).
#
# P.S. Implement the program using try/except/finally blocks.


x, y = input().split()
try:
    res = int(x) + int(y)
except:
    try:
        res = float(x) + float(y)
    except:
        res = x + y
finally:
    print(res)
