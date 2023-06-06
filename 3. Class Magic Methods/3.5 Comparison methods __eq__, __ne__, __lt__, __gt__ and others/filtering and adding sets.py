# You are faced with the task of selecting files with certain extensions from a list of files, for example:
#
# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
#               "eq_2.xls"]
#
# To do this, you must declare the FileAcceptor class, the objects of which are created by the command:
#
# acceptor = FileAcceptor(ext1, ..., extN)
#
# where ext1, ..., extN are strings with valid file extensions, for example: 'jpg', 'bmp', 'jpeg'.
#
# After that, it is supposed to use the acceptor object in the standard Python filter function as follows:
#
# filenames = list(filter(acceptor, filenames))
#
# That is, the acceptor object must be called as a function:
#
# acceptor(filename)
#
# and return True if the file named filename contains the extensions specified when the acceptor was created,
# and False otherwise. In addition, the following statement must be executed with objects of the FileAcceptor class:
#
# acceptor12 = acceptor1 + acceptor2
#
# Here, a new acceptor12 object is formed with unique extensions of the first and second objects. For example:
#
# acceptor1 = FileAcceptor("jpg", "jpeg", "png")
# acceptor2 = FileAcceptor("png", "bmp")
# acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
#
# An example of using the class (you do not need to write these lines in the program):
#
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# filenames = list(filter(acceptor_images + acceptor_docs, filenames))


class FileAcceptor:
    def __init__(self, *args):
        self.list_extensions = [] + list(args)

    def __call__(self, arg):
        return True if arg.split('.')[-1] in self.list_extensions else False

    def __add__(self, other):
        return FileAcceptor(*(set(self.list_extensions) | set(other.list_extensions)))


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
             "eq_2.xls"]
acceptor = FileAcceptor('jpg', 'bmp', 'jpeg')
acceptor1 = FileAcceptor('bmp', 'jpeg')
acceptor2 = FileAcceptor('png', 'bmp')
acceptor12 = acceptor1 + acceptor2
filenames = list(filter(acceptor12, filenames))
print(filenames)
