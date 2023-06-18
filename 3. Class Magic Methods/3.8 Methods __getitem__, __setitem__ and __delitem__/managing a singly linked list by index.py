# Previously, you have already created a stack-like structure, when one object refers to the next one,
# and so on through the chain to the last one:
#
# To do this, the program declared two classes:
#
# StackObj - for describing stack objects;
# Stack - for managing a stack-like structure.
#
# And, further, objects of the StackObj class should have been created with the command:
#
# obj = StackObj(data)
#
# where data is a string with some object content (data). In addition, each object of the StackObj class
# must have the following local attributes:
#
# data - link to a string with the data specified when creating the object;
# next - a reference to the next object of the StackObj class (when an object is created, it takes the value None).
#
# The Stack class is supposed to be used like this:
#
# st = Stack() # creating a stack-like structure object
#
# Every Stack object must have a local public attribute:
#
# top - a reference to the first stack object (if the stack is empty, then top = None).
#
# And in the Stack class itself, the following methods:
#
# push(self, obj) - adding an object of the StackObj class to the end of the stack;
# pop(self) - retrieve the last object and remove it from the stack;
#
# Additionally, in the Stack class, magic methods must be declared to access the stack object by its index, for example:
#
# obj_top = st[0] # getting the first object
# obj = st[4] # getting the 5th stack object
# st[2] = StackObj('obj3') # replacing the old (3rd) stack object with the new one
#
# If the index is not an integer, or the number is less than zero or greater than the number of objects on the stack,
# then an exception must be thrown with the command:
#
# raise IndexError('invalid index')
#
# An example of using the Stack and StackObj classes (do not write these lines in the program):
#
# st = Stack()
# st.push(StackObj('obj1'))
# st.push(StackObj('obj2'))
# st.push(StackObj('obj3'))
# st[1] = StackObj('new obj2')
# print(st[2].data) #obj3
# print(st[1].data) # new obj2
# res = st[3] # IndexError exception


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.__count_objs = 0

    def push(self, obj):
        last = self[self.__count_objs - 1] if self.__count_objs > 0 else None

        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

        self.__count_objs += 1

    def pop(self):
        if self.__count_objs == 0:
            return None

        last = self[self.__count_objs - 1]

        if self.__count_objs == 1:
            self.top = None
        else:
            self[self.__count_objs - 2].next = None

        self.__count_objs -= 1
        return last

    def __check_index(self, indx):
        if type(indx) != int or not (0 <= indx < self.__count_objs):
            raise IndexError('invalid index')

    def __getitem__(self, item):
        self.__check_index(item)
        count = 0
        last_object = self.top
        while last_object and count < item:
            last_object = last_object.next
            count += 1

        return last_object

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)
print(st[1].data)
# res = st[3]
