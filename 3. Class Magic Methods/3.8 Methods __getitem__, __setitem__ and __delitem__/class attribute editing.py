# Declare a class Record, which describes one arbitrary record from the database.
# Objects of this class are created by the command:
#
# r = Record(field_name1=value1,... , field_nameN=valueN)
#
# where field_nameX is the name of the database field; valueX - field value from the database.
#
# In each object of the Record class, local public attributes should be automatically created by field names
# (field_name1, ... , field_nameN) with the corresponding values. For example:
#
# r = Record(pk=1, title='Python OOP', author='Balakirev')
#
# Attributes appear in the r object:
#
# r.pk # 1
# r.title # Python OOP
# r.author # Balakirev
#
# It is also necessary to provide access to these fields (read / write) through indexes as follows:
#
# r[0] = 2 # access to field pk
# r[1] = 'OOP Super Course' # access to the title field
# r[2] = 'Balakirev S.M.' # access to the author field
# print(r[1]) # OOP Super Course
# r[3] # an IndexError is thrown
#
# If an invalid index is specified (not an integer or an invalid integer),
# then an exception should be thrown with the command:
#
# raise IndexError('invalid field index')
#
# P.P.S. To create local attributes, use the __dict__ collection of the Record class object.


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__total_attrs = len(kwargs)
        self.__attrs = tuple(self.__dict__.keys())

    def __check_index(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx < self.__total_attrs):
            raise IndexError('invalid field index')

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.__attrs[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.__attrs[key], value)


r = Record(pk=1, title="Python OOP", author="Balakirev")
r[0] = 2
r[1] = "Super course on OOP"
r[2] = "Balakirev S.M."
print(r[1])
r[3]
