# In Python, there is another common way to declare abstract class methods through
# the abstractmethod decorator of the abc module:
#
# from abc import ABC, abstractmethod
#
# For the abstractmethod decorator to work correctly, the class itself must be inherited from the base class ABC.
# For example, like this:
#
# class Transport(ABC):
#     @abstractmethod
#     def go(self):
#         ''Method to move the vehicle''
#
#     @classmethod
#     @abstractmethod
#     def abstract_class_method(cls):
#         ''Abstract class method''
#
# We have two abstract methods here inside the Transport class, where the first go() method is a normal method
# and the second abstract_class_method() is a class level abstract method. Pay attention to the order in which
# the classmethod and abstractmethod decorators are used. They must be written in that order.
#
# Now, if you declare any child class, for example:
#
# class Bus(Transport):
#     def __init__(self, model, speed):
#         self._model = model
#         self._speed = speed
#
#     def go(self):
#         print('bus go')
#
#     @classmethod
#     def abstract_class_method(cls):
#         pass
#
# Then it is necessary to override the abstract methods go and abstract_class_method of the Transport class in it.
# Otherwise, the object of class Bus will not be created (a TypeError exception will be raised).
#
# Using this information, declare the base class Model,
# in which you need to declare one abstract method with a signature:
#
# def get_pk(self): ...
#
# and one regular method:
#
# def get_info(self): ...
#
# which would return the string 'Model base class'.
#
# Based on the Model class, declare a child class ModelForm whose objects are created by the command:
#
# form = ModelForm(login, password)
#
# where login is the header before the login input field (string); password - title before the password entry
# field (string). In each object of the ModelForm class, local attributes with the names _login and _password
# should be generated, and a local _id attribute with a unique integer value should automatically appear
# for each object of the ModelForm class.
#
# In the ModelForm class, override the method:
#
# def get_pk(self): ...
#
# which should return the value of the _id attribute.
#
# An example of using classes (you do not need to write these lines in the program):
#
# form = ModelForm('Login', 'Password')
# print(form.get_pk())
from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return "Base class Model"


class ModelForm(Model):
    last_id = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.last_id + 1
        ModelForm.last_id += 1

    def get_pk(self):
        return self._id


form = ModelForm("login", "password")
print(form.get_pk())
