# Declare a class named Dictionary and define the following attributes in it:
#
# rus: 'Питон'
# eng: 'Python'
#
# Then, using the getattr() function, read and display the value of the rus_word attribute.
# If there is no such attribute in the class, then the getattr() function must return the boolean value False.


class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))
