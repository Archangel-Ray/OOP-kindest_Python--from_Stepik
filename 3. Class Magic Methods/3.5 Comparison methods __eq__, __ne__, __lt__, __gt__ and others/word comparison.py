# Your task is to write a program to search for a word in a string. The task is complicated by the fact that the word
# must be defined in its various forms. For example, the word:
#
# программирование
#
# may take the following forms:
#
# программирование, программированию, программированием, программировании, программирования, программированиям,
# программированиями, программированиях
#
# To solve this problem, it is necessary to declare the class Morph (morphology), the objects of which are created
# by the command:
#
# mw = Morph(word1, word2, ..., wordN)
#
# where word1, word2, ..., wordN are the possible forms of the word.
#
# In the Morph class implement methods:
#
# add_word(self, word) - adding a new word (if it is not in the word list of the Morph class object);
# get_words(self) - get a tuple of word forms.
#
# Also, the following comparison operators must be performed with objects of the Morph class:
#
# mw1 == 'word' # True if the mv1 object contains the word 'word' (case insensitive)
# mw1 != 'word' # True if the mv1 object does not contain the word 'word' (case insensitive)
#
# And a similar pair of comparisons:
#
# 'word' == mw1
# 'word' != mw1
#
# After creating the Morph class, a dict_words list is formed from objects of this class,
# for the following words with their word forms:
#
# - связь, связи, связью, связей, связям, связями, связях
# - формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
# - вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
# - эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
# - день, дня, дню, днем, дне, дни, дням, днями, днях
#
# Then, read a line from the input stream with the command:
#
# text = input()
#
# Find all occurrences of words from the list dict_words (using comparison operators) in the string text
# (case-insensitive, punctuation marks and their word forms). Display the resulting number on the screen.


class Morph:
    def __init__(self, *args):
        self._words = list(map(lambda x: x.strip(" .,!?;:").lower(), args))

    def add_word(self, word):
        w = word.lower()
        if w not in self._words:
            self._words.append(w)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other):
        if type(other) != str:
            raise ValueError("must be a string")
        return other.lower() in self._words


dict_words = [Morph("связь", "связи", "связью", "связей", "связям", "связями", "связях"),
              Morph("формула", "формулы", "формуле", "формулу", "формулой", "формул", "формулам", "формулами",
                    "формулах"),
              Morph("вектор", "вектора", "вектору", "вектором", "векторе", "векторы", "векторов", "векторам",
                    "векторами", "векторах"),
              Morph("эффект", "эффекта", "эффекту", "эффектом", "эффекте", "эффекты", "эффектов", "эффектам",
                    "эффектами", "эффектах"),
              Morph("день", "дня", "дню", "днем", "дне", "дни", "дням", "днями", "днях")]
text = "Мы будем устанавливать связь завтра днем."
words = map(lambda x: x.strip("?!:;,.").lower(), text.split())
res = sum(word == morth for word in words for morth in dict_words)
print(res)
