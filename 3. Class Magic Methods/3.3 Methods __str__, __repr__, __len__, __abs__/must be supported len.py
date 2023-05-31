# Declare a class LinkedList (linked list) to work with the following data structure:
#
# This creates a list of interconnected objects of class ObjList. Objects of this class are created by the command:
#
# obj = ObjList(data)
#
# where data is a string with some information. Also, the following local attributes must be created in each obj object
# of the ObjList class:
#
# __data - link to a string with data;
# __prev - link to the previous linked list object (if there is no object, then __prev = None);
# __next - a link to the next linked list object (if there is no object, then __next = None).
#
# In turn, objects of the LinkedList class must be created with the command:
#
# linked_lst = LinkedList()
#
# and contain local attributes:
#
# head - a link to the first object of the linked list (if the list is empty, then head = None);
# tail - a link to the last object of the linked list (if the list is empty, then tail = None).
#
# The class itself contains the following methods:
#
# add_obj(obj) - adding a new object obj of class ObjList to the end of the linked list;
#
# remove_obj(indx) - remove an object of class ObjList from the linked list by its ordinal number (index);
# the index is zero-based.
#
# Also, the following operations should be supported with objects of the LinkedList class:
#
# len(linked_lst) - returns the number of objects in a linked list;
# linked_lst(indx) - Returns the __data string stored in the ObjList at index indx (in a linked list).
#
# An example of using classes (you do not need to write these lines in the program):
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python OOP"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev


class ObjList:
    def __init__(self, data=""):
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = self.tail = obj
        else:
            obj.prev = self.tail
            self.tail.next = obj
            self.tail = obj

    def __object_by_index(self, index):
        obj = self.head
        if len(self) > index:
            if obj:
                for _ in range(index):
                    obj = obj.next
            return obj
        return None

    def remove_obj(self, index):
        obj = self.__object_by_index(index)
        if obj:
            prev_object = obj.prev
            next_object = obj.next
            if prev_object:
                prev_object.next = next_object
            else:
                self.head = next_object
            if next_object:
                next_object.prev = prev_object
            else:
                self.tail = prev_object

    def __len__(self):
        counter = 0
        obj = self.head
        while obj:
            counter += 1
            obj = obj.next
        return counter

    def __call__(self, index):
        obj = self.__object_by_index(index)
        if obj:
            return obj.data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(3)
linked_lst.remove_obj(0)
linked_lst.remove_obj(1)
linked_lst.remove_obj(0)
linked_lst.remove_obj(5)
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.add_obj(ObjList("Python OOP"))
print(len(linked_lst))
print(linked_lst(1))
print(linked_lst(2))
print(linked_lst(5))
linked_lst.remove_obj(3)
linked_lst.remove_obj(3)
linked_lst.remove_obj(1)
linked_lst.remove_obj(0)
print(len(linked_lst))
linked_lst.remove_obj(0)
print(len(linked_lst))
linked_lst.remove_obj(0)
print(len(linked_lst))
