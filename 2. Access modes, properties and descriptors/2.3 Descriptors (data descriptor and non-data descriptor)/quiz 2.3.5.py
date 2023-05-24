class StringField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y


db = DataBase('hi', 'low')
db.__dict__['x'] = 'top'
print(db.x)
