# It is necessary to declare the VideoItem class in the program to represent one video (for example, in youtube).
# Objects of this class must be created with the command:
#
# video = VideoItem(title, descr, path)
#
# where title - video title (string); descr - video description (string); path - path to the video file.
# In each object of the VideoItem class, the corresponding attributes must be created: title, descr, path.
#
# Then, you need to create a class for forming a video rating in points from 0 to 5.
# To do this, you need to declare another class called VideoRating, the objects of which are created by the command:
#
# rating = VideoRating()
#
# Each VideoRating class object must have a local private attribute named __rating containing
# an integer between 0 and 5 (0 by default). And for writing and reading a value from this private attribute,
# there must be a property object (property) named rating.
#
# Since the __rating attribute is an integer in the range [0; 5], then at the moment of assigning any value to it,
# it is necessary to check that the assigned value is an integer in the range [0; 5]. If this is not the case,
# then throw an exception with the command:
#
# raise ValueError('invalid value assigned')
#
# Further, each object of the VideoItem class must have a local rating attribute - an object of the VideoRating class.
#
# An example of using classes (do not write these lines in the program):
#
# v = VideoItem('Python OOP Course', 'Python OOP Detailed Course', 'D:/videos/python_oop.mp4')
# print(v.rating.rating) # 0
# v.rating.rating = 5
# print(v.rating.rating) # 5
# title = v. title
# descr = v.descr
# v.rating.rating = 6 # ValueError


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self, rating=0):
        self.rating = rating

    @staticmethod
    def __check_rating(value):
        if type(value) != int or not 0 <= value <= 5:
            raise ValueError("invalid value assigned")

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__check_rating(value)
        self.__rating = value


v = VideoItem("Python OOP Course", "Detailed Python OOP Course", "D:/videos/python_oop.mp4")
print(v.rating.rating)
v.rating.rating = 5
print(v.rating.rating)
title = v.title
descr = v.descr
v.rating.rating = 6
