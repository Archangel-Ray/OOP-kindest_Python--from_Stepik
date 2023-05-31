# Declare a class named Model whose objects are created by the command:
#
# model = Model()
#
# Declare a query() method in this class to generate a database entry. This method should be used as follows:
#
# model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)
#
# For example:
#
# model.query(id=1, fio='Sergey', old=33)
#
# All of this passed data must be stored inside the model object of the Model class. Then, when running the command:
#
# print(model)
#
# Information about the object should be output to the console in the following format:
#
# 'Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N'
#
# For example:
#
# 'Model: id = 1, fio = Sergey, old = 33'
#
# If the query() method was not called, then the following line is displayed in the console:
#
# 'model'


class Model:
    def __init__(self):
        self.database = dict()

    def query(self, **kwargs):
        self.database = kwargs

    def __str__(self):
        if self.database:
            return "Model: " + ", ".join(map(lambda value: f"{value[0]} = {value[1]}", self.database.items()))
        else:
            return "Model"



model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
