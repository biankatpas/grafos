from graphviz import Graph

class GrafoMaker:
    def __init__(self):
        self.listVertex = []
        self.listEdge = []
        self.listAdjacency = []

    def insertVertex(self, nome, grafo):
        self.listAdjacency.append(nome)
        referencia = self.listAdjacency.index(nome)
        grafo.node(nome)
        return referencia

    def insertEdge(self, vertA, vertB, referencia, grafo):
        self.listAdjacency.append(referencia)
        self.listAdjacency.append(referencia)
        #grafo.edge(vertA, vertB, referencia)
        print(self.listAdjacency)
        return referencia

    def removeVertex(self):
        print("Test")

    def removeEdge(self):
        print("Test")

    def checkAdjacency(self):
        print("Test")

    def returnEdgeElement(self):
        print("Test")

    def returnVertexElement(self):
        print("Test")

    def return2VertexReferences(self):
        print("Test")

    def printGraph(self):
        print("Test")