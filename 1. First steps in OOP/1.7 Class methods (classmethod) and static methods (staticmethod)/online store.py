# Declare the AppStore class - an online app store for iOS devices.
# The following methods must be implemented in this class:
#
# add_application(self, app) - adding a new app to the store;
# remove_application(self, app) - remove the app from the store;
# block_application(self, app) - blocking the app application
# (sets the local blocked property of the app object to True);
# total_apps(self) - Returns the total number of apps in the store.
#
# The AppStore class is supposed to be used as follows (do not write these lines in the program):
#
# store = AppStore()
# app_youtube = Application('Youtube')
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
#
# Here Application is a class that describes the application to be added with the specified name.
# Each Application class object must contain local properties:
#
# name - application name (string);
# blocked - boolean value (True - the application is blocked; False - not blocked, initially False).
#
# Decide for yourself how to store the list of applications in objects of the AppStore class.


class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self):
        self.applications = []

    def add_application(self, app):
        self.applications.append(app)

    def remove_application(self, app):
        if app in self.applications:
            self.applications.remove(app)

    def block_application(self, app):
        if app in self.applications:
            self.applications[self.applications.index(app)].blocked = True

    def total_apps(self):
        return len(self.applications)


store = AppStore()
app_youtube1 = Application("Youtube1")
app_youtube2 = Application("Youtube2")
app_youtube3 = Application("Youtube3")
app_youtube4 = Application("Youtube4")
app_youtube5 = Application("Youtube5")
store.add_application(app_youtube1)
store.add_application(app_youtube2)
store.add_application(app_youtube3)
store.add_application(app_youtube4)
store.block_application(app_youtube2)
store.block_application(app_youtube5)
store.remove_application(app_youtube1)
store.remove_application(app_youtube5)
print(*[x.__dict__ for x in store.applications], f"{store.total_apps()} apps in store", sep='\n')
