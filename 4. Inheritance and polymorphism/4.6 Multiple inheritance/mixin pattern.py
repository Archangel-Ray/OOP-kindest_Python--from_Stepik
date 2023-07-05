# Often multiple inheritance is used to populate a child class with certain functionality.
# That is, with each new base class specified, the child class gains more and more features.
# And, conversely, removing part of the base classes, the child class loses the corresponding part of the functionality.
#
# For example, the mixin pattern is actively used in the popular Django framework. In particular,
# when you need to tell the child class which requests from the client it should process
# (requests like GET, POST, PUT, DELETE, etc.). As an example, let's implement this idea in a very simplified way,
# but keeping the essence of the mixin pattern.
#
# Suppose the program already has the following set of classes:
#
# class RetriveMixin:
#     def get(self, request):
#         return 'GET: ' + request.get('url')
#
#
# class CreateMixin:
#     def post(self, request):
#         return 'POST: ' + request.get('url')
#
#
# class UpdateMixin:
#     def put(self, request):
#         return 'PUT: ' + request.get('url')
#
# Here, in each class, imitation of request processing is performed. The get() method of the RetriveMixin class
# is responsible for the GET request, the post() method of the CreateMixin class is responsible for the POST request,
# and the put() method of the UpdateMixin class is responsible for the PUT request.
#
# Next, you need to declare a class called GeneralView, in which you must specify an attribute (at the class level):
#
# allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
#
# for a list of allowed requests. And also declare the render_request method with the following signature:
#
# def render_request(self, request): ...
#
# Here request is a dictionary (request object), which must contain two keys:
#
# 'url' - address for request processing;
# 'method' - request method: 'GET', 'POST', 'PUT', 'DELETE', etc.
#
# In the render_request() method, you first need to check if the specified request in the request dictionary is
# allowed (present in the allowed_methods list). And if this is not the case, then throw an exception with the command:
#
# raise TypeError(f'Method {request.get('method')} not allowed.')
#
# Otherwise, call the method by its name:
#
# method_request = request.get('method').lower() # method name, in lower case
#
# Hint: To get a reference to a method named method_request, use the __getattribute__() magic method.
#
# To use the resulting classes, the following child class is declared in the program:
#
# class DetailView(RetriveMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
#
# You can use it, for example, as follows (do not write these lines in the program):
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html) # GET: https://stepik.org/course/116336/
#
# If you specify another method in the request:
#
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
#
# then an exception will naturally occur (you do not need to implement it in the program,
# this is already built into the Python language itself):
#
# AttributeError: 'DetailView' object has no attribute 'put'
#
# because the child class DetailView does not have a put method.
# You can fix this by specifying the appropriate base class:
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'PUT', )
#
# Now, when executing the commands:
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})
# print(html)
#
# will output:
#
# PUT: https://stepik.org/course/116336/
#
# This is how the mixin pattern works.


class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        method = request.get("method").upper()
        if method not in self.allowed_methods:
            raise TypeError(f"Method {request.get('method')} is not allowed.")

        method_request = self.__getattribute__(method.lower())
        if method_request:
            return method_request(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )
