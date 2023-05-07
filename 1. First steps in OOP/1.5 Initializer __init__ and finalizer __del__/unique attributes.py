# Declare a Graph class whose objects could be created with the command:
#
# gr_1 = Graph(data)
#
# where data is a list of numeric data (the data for the chart). When creating each instance of the class,
# the following local properties must be generated:
#
# data - a link to a list of numeric data (each object must have its own list with data,
#           you need to create a copy of the transferred list);
# is_show - boolean value (True/False) for showing (True) and hiding (False) chart data (True by default);
#
# In this class, declare the following methods:
#
# set_data(self, data) - to transfer a new list of data to the current chart;
# show_table(self) - to display data as a string from a list of numbers (numbers follow with a space);
# show_graph(self) - to display data as a graph (the method displays a message in the console:
# 'Graphic display of data: a string of numbers separated by spaces');
# show_bar(self) - to display data in the form of a bar chart (the method displays a message in the console:
# 'Bar chart: a string of numbers separated by a space');
# set_show(self, fl_show) - method to change the local property is_show to the passed fl_show value.
#
# If the local property is_show is False, then the show_table(), show_graph(), and show_bar() methods should
# display a message:
#
# 'Display data closed'
#
# Read numeric data from the input stream using the command:
#
# data_graph = list(map(int, input().split()))
#
# Create a Graph object gr with the read data set, call the show_bar() method, then the set_show()
# method with fl_show = False , and call the show_table() method. Two corresponding lines should appear on the screen.


class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print("Display data closed")

    def show_graph(self):
        if self.is_show:
            print("Graphic display of data: ", *self.data)
        else:
            print("Display data closed")

    def show_bar(self):
        if self.is_show:
            print("Bar chart: ", *self.data)
        else:
            print("Display data closed")

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
