# Declare a PrimaryKey class that should work in conjunction with the context manager as follows:
#
# with PrimaryKey() as pk:
#     raise ValueError
#
# where pk is a reference to an object of the PrimaryKey class. The PrimaryKey class should display the message 'entry'
# when entering the context manager, and print the type of exception that occurred when the context manager exits.
#
# The PrimaryKey class should be implemented in such a way that the context manager
# itself handles the raised exception.


class PrimaryKey:
    def __enter__(self):
        print("entry")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)

        return True


with PrimaryKey() as pk:
    raise ValueError
