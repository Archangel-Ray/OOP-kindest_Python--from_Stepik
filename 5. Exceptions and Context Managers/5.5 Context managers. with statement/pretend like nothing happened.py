# Declare a class Box (box), the objects of which are created by the command:
#
# box = Box(name, max_weight)
#
# where name - box name (string); max_weight - maximum total weight of items in the box (any positive number).
#
# Local attributes must be formed in each object of this class:
#
# _name - link to the name parameter;
# _max_weight - reference to the max_weight parameter;
# _things - a list of things stored in the box (initially an empty list).
#
# In the Box class, declare a method:
#
# def add_thing(self, obj)
#
# to add a new thing to the box, where obj is a tuple of two values:
#
# (item_name, item_weight)
#
# If at the time of adding a new item, the total weight of all items in the box becomes greater than
# the _max_weight value, then generate an exception with the command:
#
# raise ValueError('Total item weight exceeded')
#
# Then, declare another class BoxDefender, which should work in conjunction with the context manager as follows
# (do not write these lines in the program):
#
# box = Box('chest', 1000)
# box.add_thing(('matches', 46.6))
# box.add_thing(('shirt', 134))
#
# with BoxDefender(box) as b:
#     b.add_thing(('umbrella', 346.6))
#     b.add_thing(('tire', 500))
#     ...
#
# Here b is a reference to an object of class Box. If a ValueError exception occurs when adding things,
# then the box object must remain unchanged (with the things that were before the context manager was called).
# Otherwise, all added things remain in the box object.


class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []

    @property
    def things(self):
        return self._things

    @things.setter
    def things(self, lst):
        self._things = lst

    @property
    def total_weight(self):
        return sum(x[1] for x in self._things)

    def add_thing(self, obj):
        name, weight = obj
        if self.total_weight + weight > self._max_weight:
            raise ValueError("the total weight of things is exceeded")
        self._things.append(obj)


class BoxDefender:
    def __init__(self, box):
        self._box = box
        self._things = box.things[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self._box.things = self._things
        return False


box = Box("dower chest", 1000)
box.add_thing(("matches", 46.6))
box.add_thing(("shirt", 134))

with BoxDefender(box) as b:
    b.add_thing(("umbrella", 346.6))
    b.add_thing(("tire", 500))
