# Using the abc module information from the previous feat 6, declare a base class named StackInterface
# with the following abstract methods:
#
# def push_back(self, obj) - adding an object to the end of the stack;
# def pop_back(self) - remove the last object from the stack.
#
# Based on this class, declare a child class named Stack. Objects of this class must be created with the command:
#
# st = Stack()
#
# and in each object of this class a local attribute must be formed:
#
# _top is a reference to the first stack object (for an empty stack, _top = None).
#
# In the Stack class itself, override the abstract methods of the base class:
#
# def push_back(self, obj) - adding an object to the end of the stack;
# def pop_back(self) - remove the last object from the stack.
#
# The stack objects themselves must be defined by the StackObj class and created by the command:
#
# obj = StackObj(data)
#
# where data is the information stored in the object (string). Attributes should be automatically generated
# in each object of the StackObj class:
#
# _data - information stored in the object (string);
# _next - a reference to the next stack object (if there is no next object, then _next = None).
#
# An example of using classes (you do not need to write these lines in the program):
#
# st = Stack()
# st.push_back(StackObj("obj 1"))
# obj = StackObj("obj 2")
# st.push_back(obj)
# del_obj = st.pop_back() # del_obj - reference to the remote object (if there were no objects, then del_obj = None)
from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None


class Stack(StackInterface):
    def __init__(self):
        self._top = self._last = None

    def push_back(self, obj):
        if self._top:
            self._last._next = obj
            self._last = obj
        else:
            self._top = self._last = obj

    def pop_back(self):
        previous = last = self._top
        if last:
            if last._next:
                while last._next:
                    previous = last
                    last = last._next
                previous._next = None
                self._last = previous
            else:
                self._top = self._last = None

        return last


st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
st.push_back(StackObj("obj 3"))
st.push_back(StackObj("obj 4"))
st.pop_back()
st.pop_back()
st.pop_back()
st.pop_back()
del_obj = st.pop_back()
print(del_obj)
