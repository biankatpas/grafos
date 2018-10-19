
class Vertice:
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.adj = []
        self.precedente = 0
        self.estimativa = 9999
        # ESTE VALOR REPRESENTA INFINITO

    def add_adj_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj.append(vertex)

    def delete_adj_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj.remove(vertex)
