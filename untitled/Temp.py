GlowScript 2.7 VPython
from visual import *
from random import randint

"""
what the function does
INPUT:
    varname (type) - what [; default value]
NOTE:
    *Special notes
"""


# implementation of an undirected graph using Adjacency Lists
class Node:
    def __init__(self, value, visited=False, neighbors=None):
        """
        constructor Node
        INPUT:
            value (int) - Node's name ;
            visited (bool) - if we have visited the Node we set it to True ; default False
            neighbors (list of Nodes) - Node's adjacent neighbors ; default None
        """
        self.value = value
        self.visited = visited
        self.neighbors = neighbors

    '''   optional, if want to use objects as keys to a map
    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value
    '''

    def add_neighbor(self, v):
        """
        adds a neighbor v to Node's list.
        INPUT:
            v (Node) - what [; default value]
        NOTE:
            *Special notes
        """
        if self.neighbors is None:
            self.neighbors = []
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Edge:
    def __init__(self, start=None, end=None, weight=None):
        self.start = start
        self.end = end
        self.weight = weight

    def reverse_edge(self):
        return Edge(self.end, self.start, self.weight)


class Graph:
    """
    class Graph
    VARIABLES:
        nodes (Map:
                        key: Node's value,
                        value: list, first element is the Node, second is a vpython object
                  ) - all nodes in graph ;
        edges    (Map:
                        key: Node's value,
                        value: list of edges from that node
                  ) - all edges in graph ;
    """

    nodes = {}
    edges = {}

    def __init__(self, n=0):
        """
        constructor Graph
        INPUT:
            n (int) - num of nodes ; default 0
        """
        self.size = n

        if n != 0:

            weights = {}
            for i in range(n):
                for j in range(n):
                    index = n * i + j
                    node = Node(index)
                    self.nodes[index] = [node, sphere(pos=vector(i, j, 0), radius=0.25, color=color.orange)]
                    # label(pos=vector(i,j,0), text=index)
                    # label(pos=vector(i,j,0), text=i +", "+j)

                    weights[node.value] = [None, None]
                    if j is not n - 1:
                        weight = randint(0, 20)
                        weights[node.value][0] = weight  # vertical edge
                        curve(pos=[self.nodes[index][1].pos, vector(i, j + 1, 0)], axis=vector(1, 0, 0),
                              color=color.yellow)
                        label(pos=vector(i, 0.5 + j, 0), text=weight)

                    if i is not n - 1:
                        weight = randint(0, 20)
                        weights[node.value][1] = weight  # Give id to now how to give weight to edge, horizontal
                        curve(pos=[self.nodes[index][1].pos, vector(i + 1, j, 0)], axis=vector(1, 0, 0),
                              color=color.yellow)
                        label(pos=vector(0.5 + i, j, 0), text=weight)

            # Add neighbors to every Node, and create Edges, and save them to self
            for i in range(n):
                for j in range(n):
                    index = n * i + j
                    currentNode = self.nodes[index][0]
                    self.edges[currentNode.value] = []

                    if j is not n - 1:  # Has upper neighbors
                        newIndex = n * i + j + 1
                        neighbor = self.nodes[newIndex][0]
                        currentNode.add_neighbor(neighbor)
                        edge = Edge(currentNode, neighbor, weights[currentNode.value][0])
                        self.edges[currentNode.value][0] = edge

                    if i is not n - 1:  # Has right neighbors
                        newIndex = n * (i + 1) + j
                        neighbor = self.nodes[newIndex][0]
                        currentNode.add_neighbor(neighbor)
                        edge = Edge(currentNode, neighbor, weights[currentNode.value][1])
                        self.edges[currentNode.value][1] = edge

                    if j is not 0:  # Has lower neighbors
                        newIndex = n * i + j - 1
                        neighbor = self.nodes[newIndex][0]
                        currentNode.add_neighbor(neighbor)
                        edge = Edge(currentNode, neighbor, weights[neighbor.value][0])
                        self.edges[currentNode.value][2] = edge

                    if i is not 0:  # Has left neighbors
                        newIndex = n * (i - 1) + j
                        neighbor = self.nodes[newIndex][0]
                        currentNode.add_neighbor(neighbor)
                        edge = Edge(currentNode, neighbor, weights[neighbor.value][1])
                        self.edges[currentNode.value][3] = edge

    def changeColor(self, n, col):
        """
        what the function does
        INPUT:
        varname (type) - what [; default value]
        NOTE:
        *Special notes
        """
        xTemp = n // self.size
        yTemp = n - (xTemp * self.size)
        self.nodes[xTemp + yTemp * self.size][1].color = col
        # label(pos=vector(5,5,0), text=xTemp + yTemp * self.size)
        # self.nodes[self.size*i+j][1].color = col


g = Graph(3)

for i in range(g.size * g.size):
    rate(30)  # Frames per sec
    g.changeColor(i, color.red)
    sleep(0.7)
    g.changeColor(i, color.orange)
