# The program declares the following class for working with login/password input forms:
#
# class FormLogin:
#   def __init__(self, lgn, psw):
#       self.login = lgn
#       self.password = psw
#
#   def render_template(self):
#       return '\n'.join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
# Which is supposed to be used like this:
#
# login = FormLogin(TextInput("Login"), PasswordInput("Password"))
# html = login.render_template()
#
# It is necessary to register the TextInput and PasswordInput classes, the objects of which are formed by the commands:
#
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
#
# Each object of these classes must have the following local properties:
#
# name - name for the field (saves the passed name, for example, "Login" or "Password");
# size - input field size (integer, default 10).
#
# Also the TextInput and PasswordInput classes must have a method:
#
# get_html(self) - returns the generated HTML string in the format (1st line for the TextInput class; 2nd line for
# the PasswordInput class):
#
# <p class='login'><field name>: <input type='text' size=<field size> />
# <p class='password'><field name>: <input type='text' size=<field size> />
#
# For example, for the login field:
#
# <p class='login'>Login: <input type='text' size=10 />
#
# Also the TextInput and PasswordInput classes must have a class method (@classmethod):
#
# check_name(cls, name) - to check the correctness of the passed field name (should be called in the initializer)
# according to the following criteria:
#
# - name length is not less than 3 characters and not more than 50;
# - only characters of Russian, English alphabets, numbers and spaces can be used in names
#
# If the check fails, then throw an exception with the command:
#
# raise ValueError("incorrect field name")
#
# To check for valid characters, each class must have the CHARS_CORRECT attribute:
#
# CHARS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя' + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
# According to the assignment, only the TextInput and PasswordInput classes with the corresponding functionality need
# to be declared. Nothing more.

from string import ascii_lowercase, digits

class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if type(name) != str or len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Login"), PasswordInput("Password"))
html = login.render_template()
