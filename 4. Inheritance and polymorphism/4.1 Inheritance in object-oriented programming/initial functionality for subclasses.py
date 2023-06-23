# Another example is when the necessary initial functionality for subclasses is written in the base class.
#
# It is known that the browser (and not only) can send various types of requests to the server:
# GET, POST, PUT, DELETE, etc. Each of these types of requests is processed in the program on the server by its own
# separate method. In order not to prescribe all the necessary methods in classes each time when processing incoming
# requests, they are taken out to the base class and called from subclasses. Let's do this example.
#
# Let the program declare the following base class named GenericView:
#
# class GenericView:
#     def __init__(self, methods=('GET',)):
#         self.methods = methods
#
#     def get(self, request):
#         return ""
#
#     def post(self, request):
#         pass
#
#     def put(self, request):
#         pass
#
#     def delete(self, request):
#         pass
#
# Here, each method is responsible for handling its own type of request. The methods parameter is a tuple
# or list consisting of a set of allowed requests: strings with the names of the corresponding methods
# (usually written in capital letters).
# You need to declare a child class named DetailView whose objects can be created with commands:
#
# dv = DetailView() # default methods=('GET',)
# dv = DetailView(methods=('PUT', 'POST'))
#
# To initialize the methods attribute, you must call the GenericView base class initializer.
#
# Next, in the DetailView class, you need to define a method:
#
# def render_request(self, request, method): ...
#
# which would simulate the execution of a request received by the server. Here request is a dictionary with a set
# of request data; method - request type (string: 'get' or 'post' etc.).
#
# For example:
#
# html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
#
# the request must be processed as a GET request with the url parameter and the value 'https://site.ru/home'.
# The url parameter is required in the request dictionary for every request.
#
# In the render_request() method, it is necessary to check whether the specified method (method) is allowed
# (present in the methods collection). If this is not the case, then throw an exception with the command:
#
# raise TypeError('This request cannot be executed')
#
# If the check passes, then execute the corresponding method (or get(), or post(), or put(), etc.,
# returning the result of their work).
#
# Hint: you can use the __getattribute__() magic method or a similar getattr() function
# to get a reference to the desired method.
#
# Finally, in the DetailView child class, we need to override the get() method to handle the GET requests we need.
# In this method, you need to check that the request parameter is a dictionary. If it's not, then throw an exception:
#
# raise TypeError('request is not a dictionary')
#
# Check that the url key is present in the request dictionary. If not, then throw an exception:
#
# raise TypeError('request does not contain the required url key')
#
# If all checks pass, then return a string in the format:
#
# "url: <request['url']>"
#
# Example (these lines do not need to be written in the program):
#
# dv = DetailView()
# html = dv.render_request({'url': 'https://site.ru/home'}, 'GET') # url: https://site.ru/home


class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET', )):
        super().__init__(methods)

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError("this request cannot be fulfilled")

        function = getattr(self, method.lower(), False)
        if function:
            return function(request)

    def get(self, request):
        if type(request) != dict:
            raise TypeError("request is not a dictionary")
        if "url" not in request:
            raise TypeError("request does not contain the required url key")
        return f"url: {request['url']}"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
print(html)
