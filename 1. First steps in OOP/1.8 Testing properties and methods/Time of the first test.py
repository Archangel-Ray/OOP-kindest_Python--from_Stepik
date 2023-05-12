# Imagine that you have received an assignment from a customer. You are asked to implement a simple mock LAN,
# consisting of a set of servers connected to each other via a router.
#
# Each server can send a packet to any other server on the network. To do this, each has its own unique IP address.
# For simplicity, this is just an integer (natural) number from 1 to N, where N is the total number of servers.
# The algorithm is the following. Suppose a server with IP = 2 is going to send a packet of information to a server
# with IP = 3. To do this, it first sends a packet to the router, and then the router looks at the IP address and
# forwards the packet to the desired node (server).
#
# To implement this scheme, the program is invited to declare three classes:
#
# Server - to describe the operation of servers in the network;
# Router - to describe the operation of routers in the network (in this task, one router is required);
# Data - to describe the package of information.
#
# Servers will be created with the command:
#
# sv = Server()
#
# At the same time, the unique IP address of each server should be generated automatically when a new instance
# of the Server class is created.
#
# Next, the router must be created with a similar command:
#
# router = Router()
#
# Data packets, with the command:
#
# data = Data(string with data, destination IP address)
#
# For the formation and functioning of a local network, the following methods must be implemented in the Router class:
#
# link(server) - to connect the server server (an object of the Server class) to the router (for simplicity, each
# server is connected to only one router);
# unlink(server) - to disconnect the server server (an object of the Server class) from the router;
# send_data() - to send all packets (objects of the Data class) from the router's buffer to the corresponding
# servers (the buffer must be cleared after sending).
#
# And one required local property (there may be other properties):
#
# buffer - a list for storing packets received from servers (objects of the Data class).
#
# The Server class must contain its own set of methods:
#
# send_data(data) - to send an information packet data (an object of the Data class) with the specified IP address
# of the recipient (the packet is sent to the router and stored in its buffer - local buffer property);
# get_data() - returns a list of received packets (if nothing was received, then an empty list is returned)
# and clears the input buffer;
# get_ip() - returns your IP address.
#
# Accordingly, objects of the Server class must have local properties:
#
# buffer - list of received packets (objects of Data class, initially empty);
# ip - IP address of the current server.
#
# Finally, Data objects must contain the following two local properties:
#
# data - transmitted data (string);
# ip - destination IP address.
#
# An example of using these classes (you do not need to write these lines in the program):
#
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
#
# Your task is to implement the Router, Server and Data classes in accordance with the given terms of reference (TOR).
# You don't need to display anything on the screen.


class Data:
    def __init__(self, package, ip):
        self.data = package
        self.ip = ip


class Server:
    ip_server = 1

    def __init__(self):
        self.buffer = []
        self.ip = Server.ip_server
        Server.ip_server += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        copy_buffer = self.buffer[:]
        self.buffer.clear()
        return copy_buffer

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        disconnection = self.servers.pop(server.ip, False)
        if disconnection:
            disconnection.router = None

    def send_data(self):
        for record in self.buffer:
            if record.ip in self.servers:
                self.servers[record.ip].buffer.append(record)
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
