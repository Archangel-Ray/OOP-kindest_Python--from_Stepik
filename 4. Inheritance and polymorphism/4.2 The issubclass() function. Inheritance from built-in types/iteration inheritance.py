# Declare a base class in your program named IteratorAttrs to iterate over all local attributes of class objects.
# Let me remind you that two magic methods are used for this:
#
# __iter__() - to get an iterator object (in this case, this is the self object itself)
# __next__() - to iterate over the local attributes of the self object (use the __dict__ dictionary for this)
#
# The __next__() method on each iteration must return a tuple in the format: (attribute name, value).
#
# Hint: Here you can define one __iter__() method as a generator function.
#
# Declare a SmartPhone child class whose objects are created by the command:
#
# phone = SmartPhone(model, size, memory)
#
# where model - smartphone model (string); size - dimensions (width, length) as a tuple of two numbers;
# memory - size of RAM (memory), as an integer. In each object of the SmartPhone class, the corresponding
# local attributes must be created: model, size, memory.
#
# Due to inheritance from the base class IteratorAttrs,
# the for statement must be executed with objects of the SmartPhone class:
#
# for attr, value in phone:
#     print(attr, value)


class IteratorAttrs:
    def __iter__(self):
        for x in self.__dict__.items():
            yield x


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone("model", "size", "memory")
for attr, value in phone:
    print(attr, value)
