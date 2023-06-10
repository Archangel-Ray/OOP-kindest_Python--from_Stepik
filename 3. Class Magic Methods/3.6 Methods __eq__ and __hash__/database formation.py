# Declare a class named DataBase (database - DB), whose objects are created by the command:
#
# db = DataBase(path)
#
# where path is the path to the database data file (string).
#
# Also, the following methods must be declared in the DataBase class:
#
# write(self, record) - to add a new record to the database, represented by the record object;
# read(self, pk) - reading a record from the database (returns a Record object) by its unique identifier
# pk (unique positive integer); the entry is looked up in the dictionary values ​​(see below)
#
# Each database record must be described by the Record class, and objects of this class must be created by the command:
#
# record = Record(fio, descr, old)
#
# where fio - full name of some person (string); descr - person's characteristic (string); old - person's age (integer).
#
# The following local attributes must be formed in each object of the Record class:
#
# pk - record unique identifier (number: integer, positive); generated automatically when creating each new object;
# fio - person's full name (string);
# descr - person's characteristic (string);
# old - person's age (integer).
#
# Implement hash calculation for objects of class Record by attributes: fio and old (case insensitive).
# If they are the same for different records, then the hashes should be equal. Also, for objects of the Record
# class with the same hashes, the == operator must return the True value, and with different hashes - False.
#
# Records should be stored in the database in the form of a dict_db dictionary (an attribute
# of the db object of the DataBase class), the keys of which are objects of the Record class,
# and the values ​​are a list of objects with equal hashes:
#
# dict_db[rec1] = [rec1, rec2, ..., recN]
#
# where rec1, rec2, ..., recN are Record class objects with the same hashes.
#
# To populate the database, read the lines from the input stream using the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# where each line is in the format:
#
# 'Name; characteristic; age'
#
# For example:
#
# Balakirev S.M.; programmer; 33
# Kuznetsov A.V.; illegal scout; 35
# Suvorov A.V.; commander; 42
# Ivanov I.I.; a person involved in all such lists; 26
# Balakirev S.M.; teacher; 37
#
# Each row must be represented by an object of the Record class and written to the db database
# (to the db.dict_db dictionary).


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


class Record:
    record_count = 0

    def __init__(self, fio, descr, old):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__count()

    @classmethod
    def __count(cls):
        cls.record_count += 1
        return cls.record_count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = [
    "Balakirev S.M.; programmer; 33",
    "Kuznetsov A.V.; illegal scout; 35",
    "Suvorov A.V.; commander; 42",
    "Ivanov I.I.; a person involved in all such lists; 26",
    "Balakirev S.M.; teacher; 37"
]

db = DataBase("")
for string in lst_in:
    attributes = list(map(str.strip, string.split(";")))
    attributes[-1] = int(attributes[-1])
    db.write(Record(*attributes))
print(db)
