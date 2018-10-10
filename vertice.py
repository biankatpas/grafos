
class Vertice:
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.adj = []

    def add_adj_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj.append(vertex)

    def delete_adj_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj.remove(vertex)
