# You need to declare a decorator class named Handler that could be applied to functions like this:
#
# @Handler(methods=('GET', 'POST')) # default methods = ('GET',)
# def contact(request):
#   return 'Sergey Balakirev'
#
# Here, the methods argument of the Handler decorator contains a list of allowed requests to process.
# The decorated function itself is called by analogy with the previous feat:
#
# res = contact({'method': 'POST', 'url': 'contact.html'})
#
# As a result, the contact function should return a string in the format:
#
# "<method>: <data from function>"
#
# In our example, this would be:
#
# 'POST: Sergey Balakirev'
#
# If the method key is not present in the request dictionary, then a GET request is assumed by default.
# If the method key takes a value that is not in the methods list of the Handler decorator, such as 'PUT',
# then the decorated contact function must return None.
#
# To simulate GET and POST requests in the Handler class, you must declare two helper methods with signatures:
#
# def get(self, func, request, *args, **kwargs) - to simulate processing a GET request
# def post(self, func, request, *args, **kwargs) - to simulate processing a POST request
#
# Depending on the request type, the corresponding method should be called (its choice in the class can be implemented
# by the __getattribute__() method). At the output, these methods must form strings in the specified format.
#
# P.S. In the program it is enough to declare only a class. You don't need to display anything on the screen.
#
# A little help
# To implement a decorator with class-level parameters, in the __init__(self, methods) initializer, we specify
# a parameter for the decorator, and declare the __call__() magic method as
# a full-fledged decorator at the function level


class Handler:
    def __init__(self, methods=("GET", )):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request):
            m = request.get("method", "GET")
            if m in self.methods:
                method = m.lower()
                return self.__getattribute__(method)(func, request)
        return wrapper

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"


@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Sergey Balakirev"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
