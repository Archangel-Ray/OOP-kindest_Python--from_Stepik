# You need to implement a singly linked list (not a list of the Python language, do not store objects in the list,
# but form a linked structure shown in the figure) from objects of the ListObject class:
#
# To do this, declare the ListObject class in the program, the objects of which are created by the command:
#
# obj = ListObject(data)
#
# Each object of the ListObject class must contain local properties:
#
# next_obj - link to the next attached object (if there is no next object, then next_obj = None);
# data - object data as a string.
#
# In the ListObject class itself, a method must be declared:
#
# link(self, obj) - to attach an obj object of the same class to the current self object (that is, the next_obj
# attribute of self must refer to obj).
#
# Read the list of strings from the input stream with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# Then form a singly linked list whose objects (in the data attribute) store the strings from the lst_in
# list (the first string in the first object, the second string in the second, and so on). The first added object
# of the ListObject class must be referenced by the head_obj variable.


class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj


lst_in = ['1. First steps in OOP',
          '1.1 How to take this course',
          '1.2 The concept of OOP in simple terms',
          '1.3 Classes and objects. Class and Object Attributes',
          '1.4 Class methods. Parameter self',
          '1.5 The init initializer and del finalizer',
          '1.6 Magic method new. Singleton pattern example',
          '1.7 Class methods (classmethod) and static methods (staticmethod)'
          ]
head_obj = ListObject(lst_in[0])
last_object = head_obj
for ind in range(1, len(lst_in)):
    new_object = ListObject(lst_in[ind])
    last_object.link(new_object)
    last_object = new_object
