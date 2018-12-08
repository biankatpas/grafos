from graphviz import Graph


class GrafoMaker:
    def __init__(self, debug=None):
        self.debug = debug
        self.graph = Graph ('G', filename='graph.gv')
        self.tad = []

    def insertVertex(self, vertex):
        self.tad.append({"node": vertex, "adj": []})
        self.graph.node(vertex) # draw using graphviz
        return self.reference(vertex) #referencia = posicao na lista

    def insertEdge(self, vertA, vertB, label=""):
        for i in range(0, len(self.tad)):
            if self.tad[i]["node"] == vertA:
                self.tad[i]["adj"].append(vertB)
                if self.debug:
                    print('a')
                    print(self.tad[i])
            elif self.tad[i]["node"] == vertB:
                self.tad[i]["adj"].append(vertA)
                if self.debug:
                    print('b')
                    print(self.tad[i])
        self.graph.edge(vertA, vertB, label=label) # draw using graphviz
        return label # na aresta o elemento é o valor (custo, nome, etc) da aresta

    def removeVertex(self, vertex):
        if self.debug:
            print('bfr')
            print(self.tad)
        for i in range(0, len(self.tad)):
            if self.tad[i]["node"] == vertex:
                #TODO: falta o remover todas as arestas/adj
                self.tad.pop(i)
                break
        if self.debug:
            print('aft')
            print(self.tad)

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

    def renderGraph(self):
        # self.graph.view() # render, save and show graph image
        self.graph.render(view=False) # just render and save graph image

    def reference(self, node):
        for i in range(0, len(self.tad)):
            if self.tad[i]["node"] == node:
                return i
        return None