# There is a poem represented by the following list of lines:
#
# stich = ['I'm writing to you - why else?',
#          'What else can I say?'
#          'Now, I know, in your will',
#          'Punish me with contempt.',
#          'But you, to my unfortunate share',
#          'Though keeping a drop of pity,'
#          'You won't leave me.']
#
# It is necessary to remove the symbols '–?!,.;' in each line of this verse. at the beginning and end of each word,
# and break the string into words (words are separated by one or more spaces). Based on the received list of words,
# create an object of the StringText class with the command:
#
# st = StringText(lst_words)
#
# where lst_words is a list of words from one line of the poem.
#
# Comparison operators must be implemented with objects of the StringText class:
#
# st1 st2 # True if st1 has more words than st2
# st1 = st2 # True if the number of words in st1 is greater than or equal to st2
# st1 st2 # True if the number of words in st1 is less than in st2
# st1 = st2 # True if the number of words in st1 is less than or equal to st2
#
# All objects of the StringText class (for each line of the poem) are stored in the lst_text list.
# Then, form a new list lst_text_sorted from the sorted objects of the StringText class in descending order
# of the number of words. To sort, use the standard Python sorted() function. After that,
# convert this list (lst_text_sorted) into a list of strings (objects are replaced with the corresponding strings,
# a space is placed between words).


class StringText:
    def __init__(self, list_words):
        self.list_words = list(list_words)

    def __len__(self):
        return len(self.list_words)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


stich = ["I'm writing to you - why else?",
         "What else can I say?",
         "Now, I know, in your will",
         "Punish me with contempt.",
         "But you, to my unfortunate share",
         "Though keeping a drop of pity,",
         "You won't leave me."]
strip_chars = "–?!,.;"
lst_text = [StringText(x.strip(strip_chars) for x in line.split() if len(x.strip(strip_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [" ".join(x.list_words) for x in lst_text_sorted]
for line in lst_text_sorted:
    print(line)
