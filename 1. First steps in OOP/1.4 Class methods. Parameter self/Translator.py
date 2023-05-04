# Declare a class named Translator (for English to Russian translation) with the following methods:
#
# add(self, eng, rus) - to add a new pair of English and Russian words (if the English word already exists, then a new
# Russian word is added as a synonym for translation, for example, go - идти, ходить, ехать); if the link eng-rus
# already exists, then you don't need to add it a second time, for example: add('go', 'идти'), add('go', 'идти');
# remove(self, eng) - to remove a link for the specified English word;
# translate(self, eng) - for translating from English into Russian (the method should return a list of Russian words
# corresponding to the translation of an English word, even if there is only one word in the list).
#
# All additions and deletions of bindings must be performed within each specific object of the Translator class, i.e.
# bindings are stored locally inside instances of the Translator class using a dictionary collection.
# (There is no need to store bindings in a __dict__ collection! Define a separate dictionary for this.)
#
# Create an instance tr of the Translator class and call the add method on the following bindings:
#
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко
#
# Then, using the remove() method, remove the link for the English word car. Use the translate() method to translate
# the word go. Print the result on the screen as a string of all Russian words associated with the word go:
#
# Output in the format: идти ехать ходить


class Translator:
    def add(self, eng, rus):
        if 'dictionary' not in self.__dict__:
            self.dictionary = dict()

        self.dictionary.setdefault(eng, [])
        if rus not in self.dictionary[eng]:
            self.dictionary[eng].append(rus)

    def remove(self, eng):
        del self.dictionary[eng]

    def translate(self, eng):
        return self.dictionary.get(eng)


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))
