# You have been tasked with developing a DatabaseConnection class to manage a connection to a database.
# Objects of this class are created by the command:
#
# conn = DatabaseConnection()
#
# In the class itself, you need to declare a method:
#
# def connect(self, login, password): ...
#
# to connect to the database.
# In this implementation, this method must set the local attribute _fl_connection_open to True:
#
# _fl_connection_open = True
#
# and throw an exception using its own ConnectionError class inherited from the Exception base class.
#
# Also in the DatabaseConnection class there should be a method:
#
# def close(self): ...
#
# to close the connection. In this method, you need to set the _fl_connection_open attribute to False.
#
# The close() method must be called every time after the work with the database is completed,
# regardless of whether any exceptions occurred or not.
#
# This functionality (automatic closing of the database connection) is supposed to be implemented through
# the context manager using the DatabaseConnection class as follows:
#
# with DatabaseConnection() as conn:
#     # context manager statements
#
# Write additionally in the DatabaseConnection class the necessary magic methods for its use
# in conjunction with the with statement.


class ConnectionError(Exception): pass


class DatabaseConnection:
    def __init__(self):
        self._fl_connection_open = False

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

