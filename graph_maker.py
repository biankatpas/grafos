from graphviz import Graph
from graphviz import Digraph
from vertice import Vertice
from aresta import Aresta

class GraphMaker:
    def __init__(self, dirigido, debug=None):
        self.dirigido = dirigido
        self.debug    = debug
        self.nodos    = []
        self.adjlist  = {}
        self.labels   = []
        self.edges    = {}
        self.vertices = {}
        self.color    = {}

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertice(vertex)
            if self.debug == 1:
                self.debugVersion()
            return "Inserido vértice: " + vertex
        return "Vértice já existe no grafo. Não inserido."

    def insert_edge(self, vertex_a, vertex_b, peso, label=None):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            if label is None:
                label = vertex_a+vertex_b
            if label not in self.edges:
                self.edges[label] = Aresta(vertex_a, vertex_b, peso)
                self.vertices[vertex_a].addAdjVertex(vertex_b)
                self.vertices[vertex_b].addAdjVertex(vertex_a)
                if self.debug == 1:
                    self.debugVersion()
                return "Inserida aresta: " + label
            return "Aresta já existe no grafo. Não inserida."
        return "Inserir os vértices primeiro."

    #TODO
    def remove_vertex(self, vertex):
        if vertex not in self.vertices:

            message = "Vértice " + vertex + " removido."
            for i in range(0, len(self.nodos)):
                message = message + "\n" + self.return_vertex_element(i)
            return message
        return "Vértice não encontrado no grafo."

    #TODO
    def remove_edge(self, reference):
        if reference < len(self.labels):
            e = self.labels[reference]
            self.labels.pop(reference)
            self.edges.pop(e)
            if self.debug >= 1:
                print(self.labels)
                print(self.edges)
            message = "Aresta " + str(reference) + " removida.\nAtenção: referências das arestas atualizadas."
            for i in range(0, len(self.labels)):
                message = message + "\n" + self.return_edge_element(i)
            return message
        return "Aresta " + str(reference) + " não encontrada no grafo."

    def check_adjacency(self, vertex_a, vertex_b):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            for i in self.edges:
                origem = self.edges[i].origem
                destino = self.edges[i].destino
                if vertex_a == origem and vertex_b == destino or vertex_a == destino and vertex_b == origem:
                    if self.debug >= 1:
                        self.debugVersion()
                    return "Verdadeiro. Os vértices " + vertex_a + " e " + vertex_b + " são adjacentes."
            return "Falso. Os vértices " + vertex_a + " e " + vertex_b + " não são adjacentes."
        return "Vértice não encontrado no grafo"

    def return_edge_element(self, edge):
        if edge in self.edges:
            return "Elemento armazenado na aresta " + edge + " é: " + edge + " e tem peso: " + self.edges[edge].peso
        return "Aresta " + edge + " não encontrada no grafo."

    def return_vertex_element(self, vertex):
        if vertex in self.vertices:
            return "Elemento armazenado no vértice " + vertex + " é: " + self.vertices[vertex].name
        return "Vértice " + vertex + " não encontrado no grafo."

    def return_vertices_references_from_edge(self, edge):
        if edge in self.edges:
            e = self.edges[edge]
            if self.debug >= 1:
                self.debugVersion()
            return "As referências dos vértices da aresta " + edge + " são: " + e.origem + ", " + e.destino + "."
        return "Aresta " + edge + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        if self.dirigido == True:
            gv = Digraph('G', filename='graph.gv', format='png')
        else:
            gv = Graph('G', filename='graph.gv', format='png')
        for v in self.vertices:
            gv.node(self.vertices[v].name)
        for e in self.edges:
            gv.edge(self.edges[e].origem, self.edges[e].destino, label=e + " " + str(self.edges[e].peso))
        # gv.view()            # render, save and show graph image
        gv.render(view=False)  # just render and save graph image

    def debugVersion(self):
        print("Dict vertices: " + str(self.vertices))
        print("Dict edges: " + str(self.edges))
        for i in self.vertices:
            print("Vertice: " + i + "   Adjs: " + str(self.vertices[i].adj) + "   Cor Atual: " + str(self.vertices[i].color))
        print()

    # todo: algoritmos
    def check_planar_graph(self):
        return "vitor"

    def breadth_search(self, vertex):
        self.clear()
        aux = [self.vertices[vertex].name]
        self.vertices[vertex].color = 'Blue'
        while 0 != len(aux):
            u = aux[0]
            v = self.getAdjacente(u)
            if v is None:
                aux.pop(0)
            else:
                self.vertices[v].color = 'Blue'
                aux.append(v)
            self.vertices[u].color = 'Blue'
            if self.debug == 2:
                print(aux)
                self.debugVersion()
        message = "Vértices acessados: "
        for i in self.vertices:
             message += self.vertices[i].color
        print(message)
        return message

    def call_depth_search(self, vertex):
        self.clear()
        return self.depth_search(vertex)

    # TODO
    def depth_search(self, vertex):
        # print('reference',str(reference))
        print("teste para o git")
        print(vertex)
        self.vertices[vertex].color = 'Red'
        print(self.vertices[vertex].adj)
        for i in self.vertices[vertex].adj:
            print(i)
            if self.vertices[i].color == 'Black':
                print()
                self.depth_search(self.vertices[i].name)
        self.vertices[vertex] = 'Blue'
        if self.debug == 2:
            self.debugVersion()
        return "Busca em profundidade em execução. Saída no console."

    # TODO
    def prim(self, reference):
        aux = []
        for i in self.nodos:
            aux.append(i)
        aux.sort()

        while len(aux) != 0:
            u = aux[0]
            v = self.getAdjacente(u)

            if v is None:
                for i in aux:
                    self.color[i] = 'Black'
                aux.sort()
                aux.remove(u)
            else:
                w = self.getArestas(u, v)
                print(w)
                if aux.count(v) > 0:
                    print("TESTE")
        return "vitor"

    def getAdjacente(self, u):
        for i in self.vertices[u].adj:
            if self.vertices[i].color == 'Black':
                return self.vertices[i].name
        else:
            return None

    def clear(self):
        for i in self.vertices:
            self.vertices[i].color = 'Black'
        self.message = ""

    # TODO
    def getArestas(self, u, v):
        for i in self.edges:
            if u == self.edges[i][0]:
                if v == self.edges[i][1]:
                    return self.edges[i][1]
                return self.edges[i][0]
        else:
            return None