# Implement a singly linked list (not a Python list, don't use a Python list to store objects) where one object refers
# to the next one, and so on up to the last one:
#
# To do this, declare two classes in the program:
#
# StackObj - for describing singly linked list objects;
# Stack - for managing a singly linked list.
#
# Objects of the StackObj class are supposed to be created by the command:
#
# obj = StackObj(data)
#
# Here data is a string with some content. Each StackObj object must have the following local private attributes:
#
# __data - a link to a string with the data specified when creating the object;
# __next - a link to the next object of the StackObj class (when an object is created, it takes the value None).
#
# Also, property objects must be declared in the StackObj class:
#
# next - for writing and reading information from the local private property __next;
# data - for writing and reading information from the local private property __data.
#
# When writing, you need to implement a check that __next will refer to an object of the StackObj class or the value
# None. If the check fails, then __next is left unchanged.
#
# The Stack class is supposed to be used like this:
#
# st = Stack() # creating a singly linked list object
#
# Stack objects must have a local public attribute:
#
# top - a link to the first added singly linked list object (if the list is empty, then top = None).
#
# And in the Stack class itself, the following methods:
#
# push(self, obj) - adding an object of class StackObj to the end of a singly linked list;
# pop(self) - extracting the last object and removing it from the singly linked list;
# get_data(self) - get a list of objects in a singly linked list (a list of the strings of the local __data attribute
# of each object in the order they were added, or an empty list if there are no objects).
#
# An example of using the Stack and StackObj classes (these lines do not need to be written in the program):
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, following):
        if self.verification():
            self.__next = following

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if self.verification():
            self.__data = data

    def verification(self):
        if type(self) is StackObj or self is None:
            return True
        return False


class Stack:
    def __init__(self):
        self.top = None

    def push(self, facility):
        if self.top:
            last = self.top
            while last.next:
                last = last.next
            last.next = facility
        else:
            self.top = facility

    def pop(self):
        if self.top:
            previous = self.top
            last = previous.next
            if last:
                while last.next:
                    previous = last
                    last = last.next
                facility = last
                previous.next = None
            else:
                facility = self.top
                self.top = None
        else:
            return
        return facility

    def get_data(self):
        last = self.top
        list_data = []
        while last:
            list_data.append(last.data)
            last = last.next
        return list_data


obj = StackObj("obj-0")
print(obj.__dict__)
obj.data = "obj-0.1"
print(obj.data)
stack_list = Stack()
stack_list.push(obj)
stack_list.push(StackObj("obj1"))
stack_list.push(StackObj("obj2"))
stack_list.push(StackObj("obj3"))
print(stack_list.get_data())
print(stack_list.pop().__dict__)
print(stack_list.pop().__dict__)
print(stack_list.pop().__dict__)
print(stack_list.pop().__dict__)
print(stack_list.pop())
print(stack_list.get_data())
print(stack_list.__dict__)
