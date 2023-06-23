# Using the inheritance mechanism, you are instructed to develop functionality for building neural network models.
# The general scheme of the model is very simple:
#
# The base class Layer has a local attribute next_layer that refers to the next neural network layer object
# (an object of the Layer class or any child class object). The last layer has next_layer = None.
#
# To create a sequence of layers is assumed by the commands:
#
# first_layer = layer()
# next_layer = first_layer(Layer())
# next_layer = next_layer(Layer())
# ...
#
# That is, the first_layer object of the Layer class is first created, and then it is called as a function
# to form a link with the next layer. This returns a link to the next layer and the next_layer variable refers
# to this next layer of the neural network. And so you can create as many layers as you need.
#
# Each object of the Layer class must also form a local attribute:
#
# name = 'Layer'
#
# But the Layer class itself only forms links between layers. It does not carry any other functionality.
# To fix this, the program needs to declare two more child classes:
#
# Input - formation of the input layer of the neural network;
# Dense - formation of a fully connected layer of a neural network.
#
# Of course, we will not create a neural network. Therefore, in the Input class, you only need to write an initializer
# so that its objects are created as follows:
#
# inp = Input(inputs)
#
# where inputs is the total number of inputs (an integer).
# Also, an attribute should be automatically generated in objects of the Input class:
#
# name = 'Input'
#
# (Don't forget to call the initializer of the base class Layer when doing this).
#
# Objects of the second child class Dense are supposed to be created by the command:
#
# dense = Dense(inputs, outputs, activation)
#
# where inputs is the number of inputs to the layer; outputs - number of layer outputs (integer);
# activation - activation function (string, for example: 'linear', 'relu', 'sigmoid').
# And in each object of the Dense class, an attribute should also be automatically generated:
#
# name='Dense'
#
# All these classes can be used together as follows (these lines are an example, you do not need to write):
#
# network = Input(128)
# layer = network(Dense(network.inputs, 1024, 'linear'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))
#
# Three layers of neural network are created here.
#
# Finally, to iterate through all the layers using the for loop, you must declare a separate NetworkIterator class
# to iterate (enumerate) the layers of the neural network as follows:
#
# for x in NetworkIterator(network):
#     print(x.name)
#
# Here, an object of the NetworkIterator class is created. The first object (layer) of the neural network is passed
# to the input. The object of this class is an iterator, which in the for loop sequentially
# returns the objects (layers) of the neural network.


class Layer:
    def __init__(self, name="Layer"):
        self.name = name
        self.next_layer = None

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):
    def __init__(self, inputs):
        super().__init__("Input")
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        super().__init__("Dense")
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Input(layer.inputs))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)
