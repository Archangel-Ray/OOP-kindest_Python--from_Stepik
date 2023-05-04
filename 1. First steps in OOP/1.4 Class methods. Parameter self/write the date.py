# Declare a class named Graph and methods:
#
# set_data(data) - transferring the data set for subsequent display (data - list of numeric data);
# draw() - display the data (in the same order as in the data list)
#
# and attribute:
#
# LIMIT_Y = [0, 10]
#
# The set_data() method must form the local data property of the Graph class object. The data attribute must refer
# to the list passed to the method. The draw() method must display the list as a string of space-separated numbers
# that belong to the given range of the LIMIT_Y attribute (bounds included).
#
# Create a graph_1 object of the Graph class, call the set_data() method on it, and pass in the list:
#
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
#
# Then, call the draw() method through the graph_1 object. A line should appear on the screen with the corresponding
# set of numbers written with a space. For example (output without quotes):
#
# '10 0 2 5 7'


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(*filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1], self.data))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
