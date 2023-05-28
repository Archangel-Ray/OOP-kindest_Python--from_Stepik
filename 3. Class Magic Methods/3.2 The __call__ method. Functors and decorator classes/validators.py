# Suppose we are developing a class for processing an authorization form on the server side. To do this, the following
# class was created with the name LoginForm:
#
# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""
#
#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")
#
#     def is_validate(self):
#         if not self.validators:
#             return True
#
#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False
#
#         return True
#
# Here name is the title of the form (string); validators - a list of validators to check the correctness of the field.
# In the post method, the request parameter is a dictionary with the keys 'login' and 'password' and values ​​(strings)
# for the login and password, respectively.
#
# An example of using the LoginForm class (do not write in the program):
#
# from string import ascii_lowercase, digits
#
# lg = LoginForm("Enter the site", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
# lg.post({"login": "root", "password": "panda"})
# if lg.is_validate():
#     print("Further processing of form data")
#
# You need to declare validator classes in the program:
#
# LengthValidator - to check the length of data in the range [min_length; max_length];
# CharsValidator - to check valid characters in a string.
#
# Objects of these classes must be created with the commands:
#
# lv = LengthValidator(min_length, max_length) # min_length - minimum allowed length; max_length - maximum allowed
# length
# cv = CharsValidator(chars) # chars - string of valid characters
# To check the validity of the data, each validator must be called as a function:
#
# res = lv(string)
# res = cv(string)
#
# and return True if the string satisfies the validator conditions and False otherwise.


from string import ascii_lowercase, digits

class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, arg):
        return self.min_length <= len(arg) <= self.max_length


class CharsValidator:
    def __init__(self, sample):
        self.sample = sample

    def __call__(self, arg):
        for letter in arg:
            if letter not in self.sample:
                return False
        return True


lg = LoginForm("Enter the site", validators=[LengthValidator(3, 50), CharsValidator(ascii_lowercase + digits)])
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Further processing of form data")
