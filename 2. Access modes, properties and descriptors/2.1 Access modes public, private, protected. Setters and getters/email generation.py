# Declare an EmailValidator class to validate the validity of an email address. It is necessary to prohibit
# the creation of objects of this class: when creating instances, the value None should be returned, for example:
#
# em = EmailValidator() # None
#
# In the class itself, implement the following class methods (@classmethod):
#
# get_random_email(cls) - to generate a random email address in the format: xxxxxxx...xxx@gmail.com, where x is
# any valid character in the email (Latin letters, numbers, underscore and period);
# check_email(cls, email) - returns True if the email is correct and False otherwise.
#
# The correctness of the email string is determined by the following criteria:
#
# - allowed characters: Latin alphabet, numbers, underscores, dots and dog @ (one);
# - the length of the email before the @ symbol should not exceed 100 (one hundred inclusive);
# - the length of the email after the @ symbol should not exceed 50 (inclusive);
# - there must be at least one dot after the @ symbol;
# - there should not be two points in a row.
#
# Also in the class you need to implement a private static class method:
#
# is_email_str(email) - to check the type of the email variable, if it is a string, True is returned,
# otherwise it is False.
#
# The is_email_str() method should be used in the check_email() method before validating the email.
# If the email parameter is not a string, then check_email() returns False.
#
# An example of using the EmailValidator class (you do not need to write these lines in the program):
#
# res = EmailValidator.check_email("sc_lib@list.ru") # True
# res = EmailValidator.check_email("sc_lib@list_ru") # False

from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    valid_character = ascii_uppercase + ascii_lowercase + digits + "_.@"
    character_set_to_generate = ascii_uppercase + ascii_lowercase + digits + "_"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(ascii_uppercase + ascii_lowercase + digits + "_.@"):
            return False
        email_split = email.split("@")
        if len(email_split) != 2:
            return False
        if len(email_split[0]) > 100 or len(email_split[1]) > 50:
            return False
        if "." not in email_split[1]:
            return False
        if email.count("..") > 0:
            return False
        return True

    @classmethod
    def get_random_email(cls):
        address_length = randint(10, 100)
        return "".join(cls.character_set_to_generate[randint(0, len(cls.character_set_to_generate) - 1)]
                       for i in range(address_length)) + "@gmail.com"

    @staticmethod
    def __is_email_str(email):
        return type(email) == str


new_email = EmailValidator()
print(new_email)
print(EmailValidator.check_email("sc_lib@list.ru"))
print(EmailValidator.check_email("sc_lib@list_ru"))
print(EmailValidator.get_random_email())
