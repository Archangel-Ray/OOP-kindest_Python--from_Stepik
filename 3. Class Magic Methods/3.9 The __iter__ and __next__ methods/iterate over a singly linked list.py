# You have already done a stack-like structure several times, when objects are sequentially connected to each other:
#
# Let's finish its functionality. To do this, you still need to declare classes:
#
# Stack - to represent the stack as a whole;
# StackObj - to represent individual stack objects.
#
# The Stack class should have methods:
#
# push_back(obj) - to add a new object obj to the end of the stack;
# push_front(obj) - to add a new object obj to the front of the stack.
#
# Every Stack object must have a public attribute:
#
# top - a reference to the first stack object (if the stack is empty, top = None).
#
# Objects of the StackObj class are created by the command:
#
# obj = StackObj(data)
#
# where data is the data stored in the stack object (string).
#
# Also, each object of the StackObj class must have public attributes:
#
# data - link to object data;
# next - a reference to the next stack object (if it does not exist, then next = None).
#
# Finally, the following commands must be executed on objects of the Stack class:
#
# st = Stack()
#
# st[indx] = value # replacing old data with new ones by ordinal index (indx); counting starts from zero
# data = st[indx] # getting data from the stack object by index
# n = len(st) # get the total number of stack objects
#
# for obj in st: # iterate over stack objects (from beginning to end)
#       print(obj.data) # display data to console
#
# When working with indexes (indx), you need to check their correctness. Must be an integer between 0 and N-1,
# where N is the number of objects on the stack. Otherwise, throw an exception with the command:
#
# raise IndexError('invalid index')


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.top = self.last = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        current = self.top
        while current:
            yield current
            current = current.next

    def __len__(self):
        return sum(1 for _ in self)

    def get_obj(self, indx):
        if type(indx) != int or not (0 <= indx < len(self)):
            raise IndexError("invalid index")
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self.get_obj(item).data

    def __setitem__(self, key, value):
        self.get_obj(key).data = value


st = Stack()
st.push_back(StackObj("text - 1"))
st.push_back(StackObj("text - 2"))
st.push_back(StackObj("text - 3"))
st[1] = "text-2"
obj_2_data = st[1]
n = len(st)
for obj in st:
    print(obj.data)
print(obj_2_data)
