# You need to write a museum description program. To do this, you need to declare the Museum class, the objects
# of which are formed by the command:
#
# mus = Museum(museum name)
#
# The following local attributes must be formed in objects of this class:
#
# name - museum name (string);
# exhibits - list of exhibits (initially empty list).
#
# The Museum class itself must have methods:
#
# add_exhibit(self, obj) - adding a new exhibit to the museum (at the end of the exhibits list);
# remove_exhibit(self, obj) - removal of an exhibit from the museum
# (from the list of exhibits by the link obj - to the exhibit)
# get_info_exhibit(self, indx) - getting information about the exhibit (string) by list index (numbered from zero).
#
# Exhibits are represented by objects of their classes.
# For example, declare the following classes of exhibits in the program:
#
# Picture - for pictures;
# Mummies - for mummies;
# Papyri - for papyri.
#
# Objects of these classes must be created as follows (with the appropriate set of local attributes):
#
# p = Picture(title, artist, description)         # local attributes: name - title; author - artist; descr - description
# m = Mummies(mummy name, find location, description)     # local attributes: name - mummy name;
# location - find location; descr - description
# pr = Papyri(papyrus name, date, description) # local attributes: name - papyrus name; date - date (string);
# descr - description
#
# The get_info_exhibit() method of the Museum class must return the value of the descr attribute
# of the specified exhibit in the format:
#
# 'Exhibit description {name}: {descr}'
#
# For example:
#
# 'Exhibit description The Ninth Wave: Aivazovsky painted a super painting.'
#
# An example of using classes (you do not need to write these lines in the program - just for example):
#
# mus = Museum('Hermitage')
# mus.add_exhibit(Picture('Balakirev writes a letter to a foreign sultan with subscribers', 'Unknown author',
# 'Inspiring, frightening, exciting picture'))
# mus.add_exhibit(Mummies('Balakirev', 'Ancient Russia', 'Mummified Enlightener of the 21st Century'))
# p = Papyri('Teachings for, not gold for the sake of', 'Ancient Russia',
# 'The oldest found handwritten evidence of programming languages')
# mus.add_exhibit(p)
# for x in mus.exhibits:
# print(x.descr)


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, location, descr):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        exhibit = self.exhibits[indx]
        return f"Description of the exhibit {exhibit.name}: {exhibit.descr}"


mus = Museum("Hermitage")
mus.add_exhibit(Picture("Balakirev with subscribers writes a letter to a foreign sultan", "Unknown author",
                        "Inspiring, frightening, exciting picture"))
mus.add_exhibit(Mummies("Balakirev", "Ancient Russia", "Educator of the 21st century, awarded mummification"))
p = Papyri("Teachings for, not for gold sake", "Ancient Russia",
           "The oldest found handwritten evidence of programming languages")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
