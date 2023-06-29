# The program declares two classes and a global variable:
#
# CURRENT_OS = 'windows' # 'windows', 'linux'
#
#
# class WindowsFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # dialog box title
#         self.__path = path # initial directory with files
#         self.__exts = exts # tuple of displayed file extensions
#
#
# class LinuxFileDialog:
#     def __init__(self, title, path, exts):
#         self.__title = title # dialog box title
#         self.__path = path # initial directory with files
#         self.__exts = exts # tuple of displayed file extensions
#
# You need to declare a class named FileDialogFactory (class factory) that would, when the command is run:
#
# dlg = FileDialogFactory(title, path, exts)
#
# returned an object of the WindowsFileDialog class if CURRENT_OS equals the string 'windows', otherwise it returns
# an object of the LinuxFileDialog class. An object of the FileDialogFactory class itself should not be created.
#
# To implement this logic, declare two static methods inside the FileDialogFactory class:
#
# def create_windows_filedialog(title, path, exts) - to create objects of the WindowsFileDialog class;
# def create_linux_filedialog(title, path, exts) - to create objects of the LinuxFileDialog class.
#
# These methods should be called in the __new__() magic method of the FileDialogFactory class.
# Think about how to do this correctly so that an object of the class itself is not created,
# but only an object of either the WindowsFileDialog class or the LinuxFileDialog class is returned.
#
# An example of using the class (do not write this line in the program):
#
# dlg = FileDialogFactory('Images', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
#
# P.S. In the program, you only need to additionally declare the FileDialogFactory class.
# You don't need to display anything on the screen.


CURRENT_OS = 'windows'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

    def __new__(cls, *args, **kwargs):
        if CURRENT_OS == "windows":
            return cls.create_windows_filedialog(*args)
        else:
            return cls.create_linux_filedialog(*args)


dlg = FileDialogFactory('images', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))
print(dlg)
