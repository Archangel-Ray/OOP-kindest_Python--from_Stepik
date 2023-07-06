# Declare a Person class whose objects only allow named local attributes
# (the restriction is set via the __slots__ collection):
#
# _fio - employee's full name (string);
# _old - employee's age (positive integer);
# _job - position held (string).
#
# The objects themselves must be created with the command:
#
# p = Person(fio, old, job)
#
# Create several following objects of this class with information:
#
# Suvorov, 52, commander
# Rachmaninoff, 50, pianist, composer
# Balakirev, 34, programmer and teacher
# Pushkin, 32, poet and writer
#
# Save all these objects as a list named persons.


class Person:
    __slots__ = ("_fio", "_old", "_job")

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job


persons = [Person("Suvorov", 52, "commander"),
           Person("Rachmaninoff", 50, "pianist, composer"),
           Person("Balakirev", 34, "programmer and teacher"),
           Person("Pushkin", 32, "poet and writer")]
print(persons)
