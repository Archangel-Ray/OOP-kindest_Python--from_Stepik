# Earlier, in one of the exploits, we created a singly linked list with objects of the StackObj class
# (when one object refers to the next one, and so on):
#
# Let's create such a data structure again. To do this, we will declare two classes:
#
# Stack - for managing a singly linked list as a whole;
# StackObj - for representing individual objects in a singly linked list.
#
# Objects of the StackObj class must be created with the command:
#
# obj = StackObj(data)
#
# where data is a string with some data.
#
# Each object of the StackObj class must have local private attributes:
#
# __data - a link to a string with the passed data;
# __next - a link to the next object of the singly linked list (if there is no next, then __next = None).
#
# Objects of the Stack class are created by the command:
#
# st = Stack()
#
# and each of them must contain a local attribute:
#
# top - a link to the first object of a singly linked list (if there are no objects, then top = None).
#
# Also, the following methods should be declared in the Stack class:
#
# push_back(self, obj) - adding an object of class StackObj to the end of a singly linked list;
# pop_back(self) - Remove the last object from a singly linked list.
#
# Additionally, you need to implement the following functionality (in these operations, you do not need to create
# copies of a singly linked list):
#
# # adding a new object of class StackObj to the end of the singly linked list st
# st = st + obj
# st += obj
#
# # adding multiple objects to the end of a singly linked list
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# In the last two lines, N objects of the StackObj class should be automatically created with data taken from the list
# (each element of the list for the next added object).


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, txt):
        self.__data = txt

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def last_obj(self):
        penult_obj = last_obj = self.top
        if last_obj:
            while last_obj.next:
                penult_obj = last_obj
                last_obj = last_obj.next
        return penult_obj, last_obj

    def push_back(self, obj):
        last_obj = self.last_obj()[1]
        if not self.top:
            self.top = obj
        else:
            last_obj.next = obj

    def pop_back(self):
        penult_obj = self.last_obj()[0]
        if penult_obj:
            if penult_obj.next:
                penult_obj.next = None
            else:
                self.top = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        for obj in other:
            self.push_back(StackObj(obj))
        return self

    def __imul__(self, other):
        return self.__mul__(other)


st = Stack()
st.push_back(StackObj("text - 1"))
st.push_back(StackObj("text - 2"))
st.push_back(StackObj("text - 3"))
st.pop_back()
st.pop_back()
st.pop_back()
st.pop_back()
st = st + StackObj("text_1")
st += StackObj("text_2")
st = st * ["text_3", "text_4", "text_5"]
st *= ["text_6", "text_7", "text_8"]
if st.top:
    st_object = st.top
    print(st_object.data, end="")
    while st_object.next:
        st_object = st_object.next
        print(", ", st_object.data, end="")
