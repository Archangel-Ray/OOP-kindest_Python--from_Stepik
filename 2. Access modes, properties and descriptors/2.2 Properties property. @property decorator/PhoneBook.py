# You create a phone book. It is defined by the PhoneBook class. Objects of this class are created by the command:
#
# p = PhoneBook()
#
# And the class itself should have the following set of methods:
#
# add_phone(phone) - adding a new phone number (to the list);
# remove_phone(indx) - remove phone number by list index;
# get_phone_list() - get a list of objects of all phone numbers.
#
# Each phone number must be represented by the PhoneNumber class.
# Objects of this class must be created with the command:
#
# note = PhoneNumber(number, fio)
#
# where number is the phone number (number) in the XXXXXXXXXXX format (eleven digits, X is a number);
# fio - full name number owner (string).
#
# Local attributes must be formed in each object of the PhoneNumber class:
#
# number - phone number (number);
# fio - full name of the owner of the phone number.
#
# You need to declare two classes PhoneBook and PhoneNumber according to the assignment.
#
# An example of using classes (you do not need to write these lines in the program):
#
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, 'Sergey Balakirev'))
# p.add_phone(PhoneNumber(21345678901, 'Panda'))
# phones = p.get_phone_list()


class PhoneBook:
    def __init__(self):
        self.__list_numer = []

    def add_phone(self, phone):
        self.__list_numer.append(phone)

    def remove_phone(self, indx):
        self.__list_numer.pop(indx)

    def get_phone_list(self):
        return self.__list_numer


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Sergey Balakirev"))
p.add_phone(PhoneNumber(21345678901, "Panda"))
phones = p.get_phone_list()
print(*[v.__dict__ for v in phones], sep='\n')
