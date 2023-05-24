# Declare a ValidateString class to validate the passed string. Objects of this class are created by the command:
#
# validate = ValidateString(min_length=3, max_length=100)
#
# where min_length is the minimum number of characters in a string; max_length - the maximum number
# of characters in a string.
# The ValidateString class must implement the following method:
#
# validate(self, string) - returns True if string is a string (type str) and string length
# is within [min_length; max_length]. Otherwise, False is returned.
#
# Declare a StringValue data descriptor for working with strings, whose objects are created by the command:
#
# st = StringValue(validator=ValidateString(min_length, max_length))
#
# Each time a value is assigned to the st object, a validator (an object of the ValidateString class) must be called
# and the correctness of the data being assigned should be checked using the validate() method. If the data
# is incorrect, the assignment is not performed (ignored).
#
# Declare a RegisterForm class with three StringValue descriptor objects:
#
# login = StringValue(...) - to enter a login;
# password = StringValue(...) - to enter a password;
# email = StringValue(...) - to enter Email.
#
# Objects of the RegisterForm class are created by the command:
#
# form = RegisterForm(login, password, email)
#
# where login, password, email - initial values ​​of login, password and Email.
# Methods must also be declared in the RegisterForm class:
#
# get_fields() - returns a list of field values ​​in the order [login, password, email];
# show() - displays a multi-line string in the console in the format:
#
# <form>
# login: <login>
# password: <password>
# Email: <email>
# </form>


class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print("<form>",
              f"Login: {self.login}",
              f"Password: {self.password}",
              f"Email: {self.email}",
              "</form>", sep="\n")


form = RegisterForm("login", "password", "email")
form.show()
print(form.get_fields())
