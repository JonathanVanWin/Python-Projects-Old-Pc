# implementation of an undirected graph using Adjacency Lists
class Vertex:
    def __init__(self, value, visited=False, neighbors=None):
        self.value = value
        self.visited = visited
        self.neighbors = neighbors

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Edge:
    def __init__(self, start=None, end=None, weight=None):
        self.start = start
        self.end = end
        self.weight = weight

    def __hash__(self):
        return hash(self.weight)

    def __eq__(self, other):
        return isinstance(other, Edge) and self.weight == other.weight

    def reverse_edge(self):
        return Edge(self.end, self.start, self.weight)


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(str(key)+' ' + str(self.vertices[key].neighbors))

'''
g = Graph()
# print(str(len(g.vertices)))

for i in range(0,4):
    g.add_vertex(Vertex(i))

edges = [21,3] #Directed graph
for edge in edges:
    g.add_edge(edge%10, edge//10)

g.print_graph()'''


class V:
    def __init__(self,v):
        self.v = v

    def __hash__(self):
        return 5#hash(self.v)

    def __eq__(self, other):
        return isinstance(other, V) #and self.v == other.v


e = V(3)
e1 = V(3)
b =[]

a = {}
a[e] = [1, "hi"]
#print(a[e1][0])

b.append(e)
if e1 not in b:
    b.append(e1)

print(len(b))
