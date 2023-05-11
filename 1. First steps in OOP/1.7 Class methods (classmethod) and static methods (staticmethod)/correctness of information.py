# Create the CardCheck class to check the correctness of information on plastic cards.
# This class must have the following methods:
#
# check_card_number(number) - checks the card number string and returns a boolean True
# if the number is in the correct format and False otherwise. The format of the number
# is as follows: XXXX-XXXX-XXXX-XXXX, where X is any digit (from 0 to 9).
# check_name(name) - checks the name string with the map user's name.
# Returns a boolean True if the name is correct, False otherwise.
#
# Name format: two words (first name and last name) separated by a space, written in capital Latin characters
# and numbers. For example, SERGEI BALAKIREV.
#
# It is supposed to use the CardCheck class as follows (do not write these lines in the program):
#
# is_number = CardCheck.check_card_number('1234-5678-9012-0000')
# is_name = CardCheck.check_name('SERGEI BALAKIREV')
#
# To check for valid characters, an attribute must be written in the class:
#
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
# Consider how to properly declare the check_card_number and check_name methods
# (with @classmethod and @staticmethod decorators).

from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + " "

    @staticmethod
    def check_card_number(number):
        flag = True
        template = "XXXX-XXXX-XXXX-XXXX"
        if len(number) == len(template):
            for x in range(len(number)):
                if template[x] == "X":
                    if number[x] not in "0123456789":
                        flag = False
                        break
                if template[x] == "-":
                    if number[x] != "-":
                        flag = False
                        break
        else:
            flag = False
        return flag

    @classmethod
    def check_name(cls, name):
        if len(name.split()) != 2:
            return False
        flag = True
        for x in name:
            if x not in cls.CHARS_FOR_NAME:
                flag = False
                break
        return flag


is_number = CardCheck.check_card_number("1230-0678-9010-0000")
is_name = CardCheck.check_name("SERGE IREV")
print(is_name, is_number)
