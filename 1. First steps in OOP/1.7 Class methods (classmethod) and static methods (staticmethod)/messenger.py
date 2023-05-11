# Declare a class for the messenger named Viber. This class should have the following methods:
#
# add_message(msg) - adding a new message to the message list;
# remove_message(msg) - remove a message from the list;
# set_like(msg) - set/unlike the msg message (i.e. change the fl_like attribute of the msg object: if there is no like,
# then it is set, if it already exists, then it is removed);
# show_last_message(number) - display last messages;
# total_messages() - returns the total number of messages.
#
# These methods are supposed to be used as follows (do not write these lines in the program):
#
# msg = Message('Hello everyone!')
# Viber.add_message(msg)
# Viber.add_message(Message('This is a Python OOP course.'))
# Viber.add_message(Message('What do you think of him?'))
# Viber.set_like(msg)
# Viber.remove_message(msg)
#
# The Message class (must also be declared) allows you to create message objects with the following
# set of local properties:
#
# text - message text (string);
# fl_like - whether or not the message was liked (boolean value True - if there is a like
# and False - otherwise, initially False);
#
# P.S. How to store the message list is up to you.


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


class Viber:
    info = {}

    @classmethod
    def add_message(cls, message):
        cls.info[id(message)] = message

    @classmethod
    def remove_message(cls, message):
        if id(message) in cls.info:
            cls.info.pop(id(message))

    @classmethod
    def set_like(cls, message):
        if id(message) in cls.info:
            message.fl_like = not message.fl_like

    @classmethod
    def show_last_message(cls, num):
        for mes in tuple(cls.info.values())[-num:]:
            print(mes.__dict__)

    @classmethod
    def total_messages(cls):
        return len(cls.info)


msg = Message("Всем привет!")
print(msg.__dict__)
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
Viber.show_last_message(2)
