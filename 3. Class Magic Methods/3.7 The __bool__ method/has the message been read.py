# Declare the class MailBox in the program, the objects of which are created by the command:
#
# mail = mailbox()
#
# Each object of this class must contain a local public attribute:
#
# inbox_list - list of received messages.
#
# Also, the MailBox class must contain a method:
#
# receive(self) - receive new messages
#
# This method must read data from the input stream with the command:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# As a result, the lst_in list is formed from strings. Each line is written in the format:
#
# 'from whom; title; text of the letter'
#
# For example:
#
# sc_lib@list.ru; From Balakirev; Good luck in IT!
# mail@list.ru; Profitable proposition; You have been approved for a loan.
# mail123@list.ru; draw; You won 1 million rubles. Transfer 30 thousand rubles to receive it.
#
# Each line of the lst_in list must be represented by an object of the MailItem class,
# the objects of which are created by the command:
#
# item = MailItem(mail_from, title, content)
#
# where mail_from - sender's email (string); title - message title (string), content - message content (string).
# In each object of the MailItem class, the corresponding local attributes (with the names: mail_from, title, content)
# must be formed. And additionally the is_read attribute (whether read) with an initial value of False.
#
# The MailItem class must implement the following method:
#
# set_read(self, fl_read) - to mark that the message has been read (the method should
# set the attribute is_read = fl_read, if True, then the letter has been read, if False, then it has not been read).
#
# Each object of the MailItem class must have a function:
#
# bool(item)
#
# which returns True for a read message and False for an unread message.
#
# Call the method:
#
# mail.receive()
# Mark the first and last mail in the mail.inbox_list as read (use the set_read method to do this).
# Then, in the program, form a list (global) named inbox_list_filtered from the read messages,
# using the standard filter() function in conjunction with the Python bool() function.


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return True if self.is_read else False


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = [
            "sc_lib@list.ru;From Balakirev;Good luck in IT!",
            "mail@list.ru; Profitable proposition; You have been approved for a loan.",
            "mail123@list.ru; draw; You won 1 million rubles. Transfer 30 thousand rubles to receive it."
        ]

        for string in lst_in:
            mail_from, title, content = string.split(";")
            self.inbox_list.append(MailItem(mail_from, title, content))


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(inbox_list_filtered)
