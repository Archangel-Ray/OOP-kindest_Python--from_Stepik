# Declare the SmartPhone class whose objects are supposed to be created with the command:
#
# sm = SmartPhone(smartphone brand)
#
# Each object must contain local attributes:
#
# model - smartphone brand (string);
# apps - a list of installed applications (initially empty).
#
# The following methods must also be declared in the SmartPhone class:
#
# add_app(self, app) - adding a new application to the smartphone (at the end of the apps list);
# remove_app(self, app) - Remove an app by reference to the app object.
#
# When adding a new application, check that it is not in the apps list (there is no object of the corresponding class).
#
# Each application must be defined by its own class. For example, declare the following classes:
#
# AppVK - VKontakte application class;
# AppYouTube - YouTube application class;
# AppPhone - The phone application class.
#
# Objects of these classes must be created as follows (with the appropriate set of local attributes):
#
# app_1 = AppVK() # name = 'VKontakte'
# app_2 = AppYouTube(1024) # name = 'YouTube', memory_max = 1024
# app_3 = AppPhone({'Balakirev': 1234567890, 'Sergei': 98450647365, 'Work': 112}) # name = 'Phone',
# phone_list = dictionary with contacts
#
# An example of using classes (do not write these lines in the program):
#
# sm = SmartPhone('Honor 1.0')
# sm.add_app(AppVK())
# sm.add_app(AppVK()) # should not be added a second time
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
# print(a.name)


class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)

class AppVK:
    def __init__(self):
        self.name = "VKontakte"


class AppYouTube:
    def __init__(self, memory_max):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
