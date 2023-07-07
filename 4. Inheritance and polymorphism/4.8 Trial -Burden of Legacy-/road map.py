# The all-seeing eye of the authorities saw that you went through another step in understanding the depths
# of the Python OOP language - inheritance. They decided to test you again and see what you are really capable of.
# Teamleader handed you the next task with a big smile.
#
# Technical task
#
# It is necessary to write a universal framework for representing undirected connected graphs and finding the shortest
# paths in them. Further, this algorithm is supposed to be used for laying routes: on maps, in the subway, and so on.
#
# For a universal description of graphs, you need to declare the following classes in the program:
#
# Vertex - to represent the vertices of the graph (on the map, these can be: buildings, stops, sights, etc.);
# Link - to describe the connection between two arbitrary graph vertices (on the map: routes, travel time, etc.);
# LinkedGraph - to represent a connected graph as a whole (the whole map).
#
# Objects of the Vertex class must be created with the command:
#
# v = vertex()
#
# and contain a local attribute:
#
# _links - list of links with other graph vertices (list of Link class objects).
#
# Also in this class there should be a property object (property):
#
# links - to get a link to the _links list.
#
# Objects of the following Link class must be created with the command:
#
# link = Link(v1, v2)
#
# where v1, v2 are objects of the Vertex class (vertices of the graph). Within each object of the Link class,
# the following local attributes must be formed:
#
# _v1, _v2 - links to objects of the Vertex class that are connected by this link;
# _dist - link length (default 1); it can be the length of the path, travel time, etc.
#
# The following property objects must be declared in the Link class:
#
# v1 - to get a link to v1;
# v2 - to get a link to v2;
# dist - to change and read the value of the _dist attribute.
#
# Finally, objects of the third class LinkedGraph must be created with the command:
#
# map_graph = LinkedGraph()
#
# Local attributes must be formed in each object of the LinkedGraph class:
#
# _links - a list of all graph links (from objects of the Link class);
# _vertex - a list of all graph vertices (from objects of the Vertex class).
#
# In the LinkedGraph class itself, you must declare (at a minimum) the following methods:
#
# def add_vertex(self, v): ... - to add a new vertex v to the _vertex list (if it is not there);
# def add_link(self, link): ... - to add a new link link to the _links list
# (if the link object with the specified vertices is not in the list);
# def find_path(self, start_v, stop_v): ... - to find the shortest path from start_v to stop_v.
#
# The find_path() method must return a list of the vertices of the shortest path and
# a list of the links of the same route as a tuple:
#
# ([vertices of the shortest path], [connections between vertices])
#
# The search for the shortest route can be done by exhaustive search using a recursive function
# (we will assume that the total number of vertices in the graph does not exceed 100).
# For those who wish to test themselves to the fullest, Dijkstra's algorithm
# for finding the shortest path in a connected weighted graph can be implemented.
#
# In the add_link() method, when adding a new link, the vertices of this link should be automatically added
# to the _vertex list if they are not there.
#
# The check for the presence of a link in the _links list should be determined by the vertices of this link.
# For example, if the list contains an object:
#
# _links = [Link(v1, v2)]
#
# then you cannot add new Link(v2, v1) or Link(v1, v2) objects to it (note that all three objects will have
# different ids, i.e. it is impossible to determine the entry into the list by id).
#
# Hint: checking for an existing relationship can be done using the filter() function and specifying
# the desired condition for selecting objects.
#
# An example of using classes in relation to the metro scheme (these lines do not need to be written in the program):
#
# map_graph = LinkedGraph()
#
# v1 = vertex()
# v2 = vertex()
# v3 = vertex()
# v4 = vertex()
# v5 = vertex()
# v6 = vertex()
# v7 = vertex()
#
# map_graph.add_link(Link(v1, v2))
# map_graph.add_link(Link(v2, v3))
# map_graph.add_link(Link(v1, v3))
#
# map_graph.add_link(Link(v4, v5))
# map_graph.add_link(Link(v6, v7))
#
# map_graph.add_link(Link(v2, v7))
# map_graph.add_link(Link(v3, v4))
# map_graph.add_link(Link(v5, v6))
#
# print(len(map_graph._links)) # 8 links
# print(len(map_graph._vertex)) # 7 vertices
# path = map_graph.find_path(v1, v6)
#
# However, in this form, it is not very convenient to apply classes for the subway map scheme. For example,
# there are no indications of station names, and the length of each segment is 1, which is not true.
#
# To fix this point and implement a program to find the shortest path in the subway between two arbitrary stations,
# declare two more child classes:
#
# class Station(Vertex): ... - to describe metro stations;
# class LinkMetro(Link): ... - to describe links between metro stations.
#
# Station class objects must be created with the command:
#
# st = Station(name)
#
# where name - station name (string). Each object of the Station class must additionally form a local attribute:
#
# name - the name of the metro station.
#
# (Remember to call the base class initializer in the child class initializer).
#
# In the Station class itself, override the __str__() and __repr__() magic methods to return the name
# of the metro station (local attribute name).
#
# Objects of the second class LinkMetro must be created with the command:
#
# link = LinkMetro(v1, v2, dist)
#
# where v1, v2 are vertices (metro stations); dist - distance between stations (any positive number).
#
# (Also, don't forget to call the base class's initializer in the initializer of this child class.)
#
# As a result, these classes should work together as follows (these lines do not need to be written in the program):
#
# map_metro = LinkedGraph()
# v1 = Station('Sretensky Boulevard')
# v2 = Station('Turgenevskaya')
# v3 = Station('Clean Ponds')
# v4 = Station('Lubyanka')
# v5 = Station('Kuznetsky Most')
# v6 = Station('Chinatown 1')
# v7 = Station('Chinatown 2')
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
#
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
#
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
#
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6) # from Sretensky boulevard to kitay-gorod 1
# print(path[0]) # [Sretensky Boulevard, Turgenevskaya, Kitay-gorod 2, Kitay-gorod 1]
# print(sum([x.dist for x in path[1]])) # 7


class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and (id(x.v2) == id(link.v2))) or
                                   (id(x.v2) == id(link.v1) and (id(x.v1) == id(link.v2))), self._links))
        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, start_v, stop_v):
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _dist_path(self, links):
        return sum([x.dist for x in links if x is not None])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in current.links:
            path = []
            links = []
            if link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])

            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]

        return best_path, best_links


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


map_metro = LinkedGraph()
v1 = Station("Sretensky Boulevard")
v2 = Station("Turgenevskaya")
v3 = Station("Chistye Prudy")
v4 = Station("Lubyanka")
v5 = Station("Kuznetsky Most")
v6 = Station("Kitay-gorod 1")
v7 = Station("Kitay-gorod 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)
print(path[0])
print(sum([x.dist for x in path[1]]))
