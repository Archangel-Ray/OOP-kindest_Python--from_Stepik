# It is required to implement a program for working with decision trees:
#
# Here, at each node of the tree, a check is made (a question is asked). If the check passes, then the transition
# to the next object is carried out according to the left arrow (with one), and otherwise - according to the right
# arrow (with zero). And so on until we reach one of the leaves of the tree (vertices without descendants).
#
# The input data is a vector (list) with binary values: 1 - yes, 0 - no. Each element of this list corresponds
# to its own question (its own top of the tree), for example:
#
# Next, this vector is applied to the decision tree, as follows. The root node 'Loves Python' has the first element
# of the vector x associated with it and contains the value 1, so we follow the left branch. We get to the top
# 'Understands OOP'. The second element of the vector x with value 0 is associated with it, therefore, we go along
# the right branch and get to the 'will be an encoder' vertex. Since this vertex is finite (leaf), we get the result
# as a string 'will be an encoder'. By analogy, the vector x is processed with other sets of values ​​0 and 1.
#
# To implement decision trees in a program, two classes must be declared:
#
# TreeObj - to describe the vertices and leaves of the decision tree;
# DecisionTree - for working with the decision tree as a whole.
#
# The DecisionTree class must implement (at least) two class-level methods (@classmethod):
#
# def predict(cls, root, x) - to build a prediction (decision tree traversal) for the vector x from the root node
# of the tree root.
# def add_obj(cls, obj, node=None, left=True) - to add vertices to the decision tree (the method must return
# the added vertex - an object of the TreeObj class);
#
# In the add_obj method, the parameters have the following values:
#
# obj - a link to a new (added) decision tree object (an object of the TreeObj class);
# node - a reference to the tree object to which node obj is attached;
# left - a flag that determines the branch of the tree (of the node object) to which the obj object is attached
# (True - to the left branch; False - to the right).
#
# An initializer should be declared in the TreeObj class:
#
# def __init__(self, index, value=None): ...
#
# where indx is the index of the vector x being checked at the top of the tree; value - the value stored in the vertex
# (takes the value None for vertices that have descendants - intermediate vertices).
#
# At the same time, the following local attributes should automatically appear in each created
# object of the TreeObj class:
#
# indx - index being checked (integer);
# value - value with data (string);
# __left - a link to the next tree object on the left branch (initially None);
# __right - a link to the next tree object on the right branch (initially None).
#
# To work with the local private attributes __left and __right, you must declare property objects
# with the names left and right.
#
# These classes are supposed to be used in the future as follows (do not write these lines in the program):
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, 'will be a programmer'), v_11)
# DecisionTree.add_obj(TreeObj(-1, 'will be encoder'), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, 'all is not lost'), v_12)
# DecisionTree.add_obj(TreeObj(-1, 'hopeless'), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # will be the programmer


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, object):
        self.__left = object

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, object):
        self.__right = object


class DecisionTree:
    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        path_map = root
        while path_map.indx >= 0:
            path_map = path_map.left if x[path_map.indx] == 1 else path_map.right
        return path_map.value


v_1_0 = DecisionTree.add_obj(TreeObj(0))
v_1_1 = DecisionTree.add_obj(TreeObj(1), v_1_0)
v_1_2 = DecisionTree.add_obj(TreeObj(2), v_1_0, False)
DecisionTree.add_obj(TreeObj(-1, "will be a programmer"), v_1_1)
DecisionTree.add_obj(TreeObj(-1, "will encode"), v_1_1, False)
DecisionTree.add_obj(TreeObj(-1, "not everything is lost"), v_1_2)
DecisionTree.add_obj(TreeObj(-1, "hopeless"), v_1_2, False)


x = [0, 0, 0]
res = DecisionTree.predict(v_1_0, x)
print(res)
