# For sequential processing of files from some list, for example:
#
# filenames = ['boat.jpg', 'web.png', 'text.txt', 'python.doc', 'ava.8.jpg', 'forest.jpeg', 'eq_1.png', 'eq_2. png',
# 'my.html', 'data.shtml']
#
# It is necessary to declare an ImageFileAcceptor class that would select only files with the specified extensions.
#
# To do this, it is supposed to create class objects with the command:
#
# acceptor = ImageFileAcceptor(extensions)
#
# where extensions is a tuple with valid file extensions, for example: extensions = ('jpg', 'bmp', 'jpeg').
#
# And then use the acceptor object in the standard Python filter function like this:
#
# image_filenames = filter(acceptor, filenames)
# An example of using the class (you do not need to write these lines in the program):
#
# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]


class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, arg):
        return arg.split('.')[-1] in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
