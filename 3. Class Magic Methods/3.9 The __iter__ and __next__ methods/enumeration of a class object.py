# Declare the Person class in the program, the objects of which are created by the command:
#
# p = Person(fio, job, old, salary, year_job)
#
# where fio - full name of the employee (string); job - job title (string); old - age (integer);
# salary - salary (number: integer or real); year_job - continuous experience at the specified job (integer).
#
# In each object of the Person class, local attributes with the same names should be automatically
# created: fio, job, old, salary, year_job and the corresponding values.
#
# The following commands should also be supported with objects of the Person class:
#
# data = p[indx] # getting data by index number (indx) of the attribute
#                  (order: fio, job, old, salary, year_job and starts from zero)
# p[indx] = value # write to the field with the specified index (indx) of the new value value
# for v in p: # iterate through all object attributes in order: fio, job, old, salary, year_job
#     print(v)
#
# When working with indexes, check if the value of indx is correct. It must be an integer in the range [0; 4].
# Otherwise, throw an exception with the command:
#
# raise IndexError('invalid index')
#
# An example of using the class (do not write these lines in the program):
#
# pers = Person('B. Gates', 'businessman', 61, 1000000, 46)
# pers[0] = 'Balakirev S.M.'
# for v in pers:
#       print(v)
# pers[5] = 123 #IndexError


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._atters = tuple(self.__dict__)
        self._len_atters = len(self._atters)
        self._iter_index = -1

    def __check_index(self, index):
        if type(index) != int or not (-self._len_atters <= index < self._len_atters):
            raise IndexError("invalid index")

    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self._atters[item])

    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self._atters[key], value)

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < self._len_atters - 1:
            self._iter_index += 1
            return getattr(self, self._atters[self._iter_index])
        raise StopIteration


pers = Person("Gates B.", "businessman", 61, 1000000, 46)
pers[0] = "Balakirev S.M."
for v in pers:
    print(v)
# pers[5] = 123 # IndexError
