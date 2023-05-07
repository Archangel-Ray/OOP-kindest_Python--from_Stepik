# Declare three classes of geometric shapes: Line, Rect, Ellipse.
# It should be possible to create objects of each class with the following commands:
#
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
#
# Here, the coordinates of the upper right and lower left corners (arbitrary numbers) are passed
# as arguments a, b, c, d. In each object, the coordinates must be stored in local properties sp (top right)
# and ep (bottom left) as tuples (a, b) and (c, d), respectively.
#
# Generate 217 objects of these classes: for each current object, a class is chosen randomly (either Line, or Rect,
# or Ellipse). Coordinates are also generated randomly (numeric values). Save all objects in the elements list.
#
# In the elements list, reset the object coordinates for the Line class only.
#
# P.S. You don't need to display anything on the screen.

from random import random, choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class_name = ['Line', 'Rect', 'Ellipse']
elements = []
for index in range(217):
    which = choice(class_name)
    if which == 'Line':
        element = Line(random(), random(), random(), random())
        elements.append(element)
    elif which == 'Rect':
        element = Rect(random(), random(), random(), random())
        elements.append(element)
    elif which == 'Ellipse':
        element = Ellipse(random(), random(), random(), random())
        elements.append(element)
for elem in elements:
    if isinstance(elem, Line):
        elem.ep = elem.sp = (0, 0)
for z in elements:
    print(z.__dict__)
print(len(elements))
