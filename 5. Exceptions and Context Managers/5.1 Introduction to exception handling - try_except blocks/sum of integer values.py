# In the program, some data is entered in one line separated by a space, for example:
#
# '1 -5.6 2 abc 0 False 22.5 hello world'
#
# This data is space-separated and presented as a list of strings:
#
# lst_in = input().split()
#
# Your task is to calculate the sum of all integer values ​​present in the lst_in list. Display the result (sum).
#
# Hint: selecting only integer values ​​can be done using the filter() function, then converting them to integers using
# the map() function, and then calculating their sum using the sum() function. To select integer values,
# it is recommended to declare an auxiliary function that would return True for strings that contain an integer
# and False for all other strings.


lst_in = input("write something: ").split()
total = 0
for value in lst_in:
    try:
        total += int(value)
    except:
        continue
print(total)
