import random


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def add_neighbor(self, vertex_name):
        self.neighbors.add(vertex_name)


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
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False

    def print(self):
        for key in sorted(list(self.vertices.keys())):
            print(key, sorted(list(self.vertices[key].neighbors)))


graph = Graph()
a = Vertex('A')
graph.add_vertex(a)
graph.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('Z') + 1):
    graph.add_vertex(Vertex(chr(i)))

graph.print()

abc = [chr(a) for a in range(ord('A'), ord('Z') + 1)]
cba = sorted(abc, reverse=True)
edges = [abc[i] + cba[i] for i in range(len(abc))]
print(edges)

for edge in edges:
    graph.add_edge(edge[0], edge[1])

graph.print()

for i in range(3):
    random.shuffle(cba)
    edges = [f'{abc[i]}{cba[i]}' for i in range(len(abc))]
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

graph.print()
