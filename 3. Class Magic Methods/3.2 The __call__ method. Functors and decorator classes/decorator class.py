# You need to declare a decorator class named HandlerGET that will simulate the processing of GET requests
# on the server side. To do this, the HandlerGET class itself needs to be designed in such a way that it can
# be applied to any function as a decorator. For example:
#
# @HandlerGET
# def contact(request):
#   return 'Sergey Balakirev'
#
# Here request is an arbitrary dictionary with the data of the current request, for example:
# {'method': 'GET', 'url': 'contact.html'}. The function must return a string.
#
# Then, when calling the decorated function:
#
# res = contact({'method': 'GET', 'url': 'contact.html'})
#
# should return a string in the format:
#
# 'GET: data from function '
#
# In our example, this would be:
#
# 'GET: Sergey Balakirev'
#
# If the method key is not present in the request dictionary, then a GET request is assumed by default. If the method
# key takes another value, such as 'POST', then the decorated contact function should return None.
#
# To implement a simulated GET request in the HandlerGET class, declare a helper method with the following signature:
#
# def get(self, func, request, *args, **kwargs): ...
#
# Here func is a reference to the function being decorated; request - a dictionary with the data passed when calling
# the decorated function. It is in this method that the returned string should be formed in the specified format:
#
# 'GET: Sergey Balakirev'


class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        m = request.get("method", "GET")
        if m == "GET":
            return self.get(self.func, request)
        return None

    def get(self, func, request):
        return f"GET: {func(request)}"


@HandlerGET
def contact(request):
    return "Sergey Balakirev"


res = contact({"method": "GET", "url": "contact.html"})
print(res)
