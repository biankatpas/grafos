
class Vertice:
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.adj = []

    def addAdjVertex(self, vertex):
        if vertex not in self.adj:
            self.adj.append(vertex)

    def deleteAdjVertex(self, vertex):
        if vertex not in self.adj:
            self.adj.remove(vertex)
