# The program declares two classes:
#
# class ShopItem:
#     ID_SHOP_ITEM = 0
#
#     def __init__(self):
#         super().__init__()
#         ShopItem.ID_SHOP_ITEM += 1
#         self._id = ShopItem.ID_SHOP_ITEM
#
#     def get_pk(self):
#         return self._id
#
#
# class Book(ShopItem):
#     def __init__(self, title, author, year):
#         super().__init__()
#         self._title = title
#         self._author = author
#         self._year = year
#
# Then, an object of class Book (book) is created and displayed in the console:
#
# book = Book('Python OOP', 'Balakirev', 2022)
# print(book)
#
# As a result, on the screen we will see something like:
#
# __main__.Book object at 0x0000015FBA4B3D00
#
# But we need to display the local attributes of the object here with their values ​​in the format:
#
# attribute_1: value_1
# attribute_2: value_2
# ...
# attribute_N: value_N
#
# To do this, you are given the task to develop two classes:
#
# ShopGenericView - to display all local attributes of objects of any child classes (not just Book);
# ShopUserView - to display all local attributes, except for the _id attribute,
# of objects of any child classes (not just Book).
#
# That is, two magic methods need to be redefined in these classes: __str__() and __repr__().
#
# An example of using classes (you do not need to write these lines in the program):
#
# class Book(ShopItem, ShopGenericView): ...
# book = Book('Python OOP', 'Balakirev', 2022)
# print(book)
# # on the screen we will see the lines:
# #_id: 1
# # _title: Python OOP
# # _author: Balakirev
# # _year: 2022
#
# Another use case for classes:
#
# class Book(ShopItem, ShopUserView): ...
# book = Book('Python OOP', 'Balakirev', 2022)
# print(book)
# # on the screen we will see the lines:
# # _title: Python OOP
# # _author: Balakirev
# # _year: 2022


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __str__(self):
        return "\n".join([f"{i}: {v}" for i, v in self.__dict__.items()])


class ShopUserView:
    def __str__(self):
        return "\n".join([f"{i}: {v}" for i, v in self.__dict__.items()][1:])


class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python OOP", "Balakirev", 2022)
print(book)
print()


class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python OOP", "Balakirev", 2022)
print(book)
