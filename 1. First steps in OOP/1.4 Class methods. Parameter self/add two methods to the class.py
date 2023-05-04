# Rows of data are read from the input stream using the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines())) # read a list of lines from the input stream
#
# in the format: id, name, old, salary (written with a space). For example:
#
# 1 Sergey 35 120000
# 2 Fedor 23 12000
# 3 Ivan 13 1200
# ...
#
# That is, each line is an element of the lst_in list.
#
# Needed in the DataBase class:
#
# class DataBase:
#   lst_data = []
#   FIELDS = ('id', 'name', 'old', 'salary')
#
# add two methods:
#
# select(self, a, b) - returns a list of elements of the lst_data list in the range [a; b] (inclusive) by their indexes
# (not id, but list indexes); also take into account that the bound b may exceed the length of the list.
# insert(self, data) - to add new data to the list lst_data from the passed list of strings data;
#
# Each entry in the lst_data list must be represented by a dictionary in the format:
#
# {'id': 'number', 'name': 'name', 'old': 'age', 'salary': 'salary'}
#
# For example:
#
# {'id': '1', 'name': 'Sergei', 'old': '35', 'salary': '120000'}
#
# Note: In this problem, the number of elements per line (separated by a space) is always the same as the number
# of fields in the FIELDS collection.
#
# P.S. Your task is only to add two methods to the DataBase class.

lst_in = ['1 Sergey 35 120000', '2 Fedor 23 12000', '3 Ivan 13 1200']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a: b+1]

    def insert(self, data):
        for value in data:
            self.lst_data.append(dict(zip(self.FIELDS, value.split())))


db = DataBase()
db.insert(lst_in)
print(db.lst_data)
