# Declare a RandomPassword class to generate random passwords. Objects of this class must be created with the command:
#
# rnd = RandomPassword(psw_chars, min_length, max_length)
#
# where psw_chars is a string of characters allowed in the password; min_length, max_length - minimum
# and maximum length of generated passwords.
#
# Direct generation of a single password must be performed by the command:
#
# psw = rnd()
#
# where psw is a reference to a string with a length in the range [min_length; max_length] from randomly selected
# characters of the string psw_chars.
#
# Using the list comprehension, create a list of lst_pass from the three generated passwords with the rnd object
# of the RandomPassword class created with the parameters:
#
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
from random import randint


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        password_length = randint(self.min_length, self.max_length)
        len_chars = len(self.psw_chars) - 1

        return "".join(self.psw_chars[randint(0, len_chars)] for _ in range(password_length))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd(), rnd(), rnd()]
print(lst_pass)
