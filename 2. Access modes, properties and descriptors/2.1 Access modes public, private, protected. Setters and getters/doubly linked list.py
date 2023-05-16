# It is necessary to implement a linked list (not a Python list and do not store objects in a Python list) when objects
# of the ObjList class are connected to their neighbors through the private properties __next and __prev:
#
#
#
# To do this, declare a LinkedList class that will represent the linked list as a whole and have a set of the following
# methods:
#
# add_obj(self, obj) - adding a new object obj of class ObjList to the end of the linked list;
# remove_obj(self) - remove the last object from the linked list;
# get_data(self) - get the list from the strings of the local __data property of all linked list objects.
#
# And in each object of this class, local public attributes must be created:
#
# head - a link to the first object of the linked list (if the list is empty, then head = None);
# tail - a link to the last object of the linked list (if the list is empty, then tail = None).
#
# Objects of class ObjList must have the following set of private local properties:
#
# __next - a link to the next linked list object (if there is no next object, then __next = None);
# __prev - link to the previous linked list object (if there is no previous object, then __prev = None);
# __data - string with data.
#
# Also, the following setters and getters must be implemented in the ObjList class:
#
# set_next(self, obj) - change the private property __next to the value of obj;
# set_prev(self, obj) - change the private property __prev to the value of obj;
# get_next(self) - getting the value of the private property __next;
# get_prev(self) - getting the value of the private property __prev;
# set_data(self, data) - change private property __data to data value;
# get_data(self) - getting the value of the private property __data.
#
# It is supposed to create objects of class ObjList by the command:
#
# ob = ObjList('data 1')
#
# And use the LinkedList class as follows (for example, you do not need to write these lines in the program):
#
# lst = LinkedList()
# lst.add_obj(ObjList('data 1'))
# lst.add_obj(ObjList('data 2'))
# lst.add_obj(ObjList('data 3'))
# res = lst.get_data() # ['data 1', 'data 2', 'data 3']
#
# Declare the LinkedList and ObjList classes in the program as appropriate.


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return "there is no one for delete"
        ptr = self.tail.get_prev()
        if ptr:
            ptr.set_next(None)
        self.tail = ptr
        if self.tail is None:
            self.head = None

    def get_data(self):
        list_data = []
        current_head = self.head
        while current_head:
            list_data.append(current_head.get_data())
            current_head = current_head.get_next()
        return list_data


lst = LinkedList()
lst.add_obj(ObjList("information 1"))
lst.add_obj(ObjList("information 2"))
lst.add_obj(ObjList("information 3"))
res = lst.get_data()
print(res)
lst.remove_obj()
lst.remove_obj()
lst.remove_obj()
print(lst.remove_obj())
