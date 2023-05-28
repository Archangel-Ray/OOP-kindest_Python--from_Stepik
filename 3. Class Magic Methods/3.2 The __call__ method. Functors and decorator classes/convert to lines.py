# Suppose you need to create a program to convert a list of strings, for example:
#
# lst = ['Menu item 1', 'Menu item 2', 'Menu item 3']
#
# into the following fragment of HTML markup (multi-line string, quotes do not need to be displayed):
#
# '''<ul>
# <li>Menu item 1</li>
# <li>Menu item 2</li>
# <li>Menu item 3</li>
# </ul>'''
#
# To do this, you need to declare the RenderList class, the objects of which are created by the command:
#
# render = RenderList(type_list)
#
# where type_list is the type of the list (takes the values: 'ul' - for a list with a tag ul and 'ol'
# - for a list with a tag ol ). If the value of the type_list parameter is different (not 'ul' and not 'ol'),
# then a list with the ul tag is formed.
#
# Then, it is supposed to use the render object like this:
#
# html = render(lst) # returns a multi-line string with appropriate HTML markup
#
# An example of using the class (you do not need to write these lines in the program):
#
# lst = ['Menu item 1', 'Menu item 2', 'Menu item 3']
# render = RenderList('ol')
# html = render(lst)


class RenderList:
    def __init__(self, marking):
        self.marking = marking if marking == "ol" else "ul"

    def __call__(self, arg):
        string_list = ["<li>" + string + "</li>\n" for string in arg]
        return f'''<{self.marking}>\n{"".join(string_list)}</{self.marking}>'''


lst = ["Menu item 1", "Menu item 2", "Menu item 3"]
print(RenderList("ol")(lst), "\n")
print(RenderList("ul")(lst), "\n")
print(RenderList("")(lst))
