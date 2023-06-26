# Your team is building a small web server framework. For this, a class was declared:
#
# class Router:
#     app = {}
#
#     @classmethod
#     def get(cls, path):
#         return cls.app.get(path)
#
#     @classmethod
#     def add_callback(cls, path, func):
#         cls.app[path] = func
#
# And it's supposed to be used like this:
#
# @Callback('/', Router)
# def index():
#     return '<h1>Main</h1>'
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)
#
# Here Callback is a decorator class with parameters: path = '/' - route; router_cls = Router - router class.
# The Callback decorator should ensure that the function (in the example index) is added to the app dictionary
# of the Router class. The dictionary key is the route (path), and the value is a reference to the function
# being decorated. To do this, use the add_callback method of the Router class.
#
# Then, the previously added function (in the example index) is selected from the router (Router) by the get method,
# and if it exists, it is called with the output of the result to the console.
#
# Your task is to implement the Callback decorator class.
#
# A little help.
#
# To implement a decorator with class-level parameters, in the __init__(self, methods) initializer,
# we specify a parameter for the decorator, and declare the __call__() magic method to decorate the function:
#
# class Handler:
#     def __init__(self, path, route_cls):
#         # here are the lines you need
#
#     def __call__(self, func):
#         # lines here


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path, router_cls):
        self.__path = path
        self.__router_cls = router_cls

    def __call__(self, func):
        self.__router_cls.add_callback(self.__path, func)
        return func


@Callback('/', Router)
def index():
    return '<h1>Main</h1>'


route = Router.get('/')
if route:
    ret = route()
    print(ret)

