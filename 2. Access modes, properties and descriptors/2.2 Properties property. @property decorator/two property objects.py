# Declare the WindowDlg class in the program, the objects of which are supposed to be created by the command:
#
# wnd = WindowDlg(window title, width, height)
# Each object of the WindowDlg class must create private local attributes:
#
# __title - window title (string);
# __width, __height - window width and height (numbers).
#
# In the WindowDlg class, you need to implement the method:
#
# show() - to display a window on the screen (outputs a string in the console in the format: ' Title : width ,
# height ', for example 'Dialogue 1: 100, 50').
#
# It is also necessary to implement two property objects in the WindowDlg class:
#
# width - to change and read the width of the window;
# height - to change and read the height of the window.
#
# When resizing a window, you need to check:
#
# - the passed value is an integer in the range [0; 10000].
#
# If at least one size has changed (height or width), then you should automatically redraw the window (call the show()
# method). There is no need to call the show() method when initializing width and height sizes.


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check(height):
            self.__height = height
            self.show()

    @classmethod
    def check(cls, num):
        if type(num) is int:
            if 0 < num < 10000:
                return True
        return False


win = WindowDlg("Menu", 10, 15)
win.show()
win.width = 100
win.height = 99999
win.height = 999
win.width = "10"
