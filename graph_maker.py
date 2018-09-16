from graphviz import Graph


class GraphMaker:
    def __init__(self, debug=None):
        self.debug    = debug
        self.nodos    = []
        self.adjlist  = {}
        self.labels   = []
        self.edges    = {}

    def insert_vertex(self, vertex):
        if vertex not in self.nodos:
            self.nodos.append(vertex)
            self.adjlist[vertex] = []
            if self.debug:
                print(self.adjlist)
            return "Inserido vértice: " + vertex + ". Referência: " + str(self.nodos.index(vertex))
        return "Vértice já existe no grafo. Não inserido."


    def insert_edge(self, vertex_a, vertex_b, label=None):
        if vertex_a in self.nodos and vertex_b in self.nodos:
            if label is None:
                label = vertex_a+vertex_b
            if label not in self.labels:
                self.labels.append(label)
                self.edges[label] = [vertex_a, vertex_b]
                self.adjlist[vertex_a].append(vertex_b)
                self.adjlist[vertex_b].append(vertex_a)
                if self.debug:
                    print(self.adjlist)
                    print(self.edges)
                return "Inserida aresta: " + label + ". Referência: " + str(self.labels.index(label))
            return "Aresta já existe no grafo. Não inserida."
        return "Inserir os vértices primeiro."

    def remove_vertex(self, reference):
        if reference < len(self.nodos):
            vertex = self.nodos[reference]
            self.nodos.pop(reference)
            self.adjlist.pop(vertex)
            for v in self.adjlist:
                if vertex in self.adjlist[v]:
                    k = self.adjlist[v].index(vertex)
                    self.adjlist[v].pop(k)
            delete = []
            for e in self.edges:
                if vertex in self.edges[e]:
                    delete.append(e)
            for d in delete:
                self.labels.remove(d)
                self.edges.pop(d)
            if self.debug:
                print(self.nodos)
                print(self.adjlist)
                print(self.labels)
                print(self.edges)
            return "Vértice " + str(reference) + " removido."
        return "Vértice não encontrado no grafo."

    def remove_edge(self, reference):
        if reference < len(self.labels):
            e = self.labels[reference]
            self.labels.pop(reference)
            self.edges.pop(e)
            if self.debug:
                print(self.labels)
                print(self.edges)
            return "Aresta " + str(reference) + " removida."
        return "Aresta " + str(reference) + "não encontrada no grafo."

    def check_adjacency(self, vertex_a, vertex_b):
        if vertex_a in self.nodos and vertex_b in self.nodos:
            adj_a = self.adjlist[vertex_a]
            adj_b = self.adjlist[vertex_b]
            if vertex_a in adj_b and vertex_b in adj_a:
                return "Verdadeiro. Os vértices " + vertex_a + " e " + vertex_b + " são adjacentes."
            if self.debug:
                print(adj_a)
                print(adj_b)
            return "Falso. Os vértices " + vertex_a + " e " + vertex_b + " não são adjacentes."
        return "Vértice não encontrado no grafo"

    def return_edge_element(self, reference):
        if reference < len(self.labels):
            return "Elemento armazenado na aresta " + str(reference) + " é: " + self.labels[reference]
        return "Aresta " + str(reference) + " não encontrada no grafo."

    def return_vertex_element(self, reference):
        if reference < len(self.nodos):
            return "Elemento armazenado no vértice " + str(reference) + " é: " + self.nodos[reference]
        return "Vértice " + str(reference) + " não encontrado no grafo."

    def return_vertices_references_from_edge(self, reference):
        if reference < len(self.labels):
            e = self.labels[reference]
            vertices = self.edges[e]
            vertex_a = self.nodos.index(vertices[0])
            vertex_b = self.nodos.index(vertices[1])
            if self.debug:
                print(e)
                print(vertices)
            return "As referências dos vértices da aresta " + str(reference) + " são: " + str(vertex_a) + "," + str(vertex_b) + "."
        else: return "Aresta " + str(reference) + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        gv = Graph('G', filename='graph.gv', format='png')
        for nodo in self.nodos:
            gv.node(nodo)
        for e in self.edges:
            gv.edge(self.edges[e][0], self.edges[e][1], label=e)
        # gv.view()               # render, save and show graph image
        gv.render(view=False) # just render and save graph image

    # todo: algoritmos
    def check_planar_graph(self):
        return "vitor"

    def breadth_search(self):
        return "vitor"

    def depth_search(self):
        return "vitor"

    def prim(self):
        return "vitor"
