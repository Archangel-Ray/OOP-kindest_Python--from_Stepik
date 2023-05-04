# There is the following class for reading information from the input stream:
#
# import sys
#
#
# class StreamReader:
#   FIELDS = ('id', 'title', 'pages')
#
#   def readlines(self):
#       lst_in = list(map(str.strip, sys.stdin.readlines())) # read a list of lines from the input stream
#       sd = StreamData()
#       res = sd.create(self.FIELDS, lst_in)
#       return sd, res
#
# Which, then, can be used as follows:
#
# sr = StreamReader()
# data,result = sr.readlines()
#
# It is necessary to declare another StreamData class with the method before the StreamReader class:
#
# def create(self, fields, lst_values): ...
#
# which at the input would receive a FIELDS tuple from the names of local attributes (passed to the fields attribute)
# and a list of lst_in strings (passed to the lst_values ​​attribute) and would form local properties in the StreamData
# class object with field names from fields and corresponding values ​​from lst_values.
#
# If the creation of local properties succeeds, then the create() method returns True, otherwise False.
# If the number of fields and the number of rows do not match, then the create() method returns False and
# no local attributes need be created.
#
# P.S. In the program, only the StreamData class needs to be additionally declared. Nothing more needs to be done.


import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for index, value in enumerate(fields):
                setattr(self, value, lst_values[index])
            return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
