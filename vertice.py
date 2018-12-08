
class Vertice:
    def __init__(self, name, pos):
        self.name = name
        self.color = 'white'
        self.adj = []
        self.precedente = None
        self.estimativa = 9999
        # ESTE VALOR REPRESENTA INFINITO
        self.position = pos

    def add_adj_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj.append(vertex)

    def delete_adj_vertex(self, vertex):
        if vertex in self.adj:
            self.adj.remove(vertex)

    def __lt__(self, other):
        return self.estimativa < other.estimativa
