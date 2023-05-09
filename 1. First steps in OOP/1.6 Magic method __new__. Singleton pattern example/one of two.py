# The program declares the TYPE_OS variable and the following two classes:
#
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#   name_class = 'DialogWindows'
#
#
# class DialogLinux:
#   name_class = 'DialogLinux'
#
# It is necessary to declare a third class named Dialog, which would create objects with the command:
#
# dlg = Dialog(<title>)
#
# Here title is a string that is stored in the local name property of the dlg object.
#
# The Dialog class must create objects of the DialogWindows class if the TYPE_OS variable = 1 and objects
# of the DialogLinux class if the TYPE_OS variable is not equal to 1. At the same time, the TYPE_OS variable
# can change in subsequent lines of the program. Keep this in mind when declaring the Dialog class.


TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        new_object = None
        if TYPE_OS == 1:
            new_object = super().__new__(DialogWindows)
        else:
            new_object = super().__new__(DialogLinux)

        new_object.name = args[0]
        return new_object


super_new_object = Dialog('name_class')
print(super_new_object.__dict__, type(super_new_object))
