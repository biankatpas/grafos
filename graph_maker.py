from graphviz import Graph
from graphviz import Digraph
from vertice import Vertice
from aresta import Aresta
import time


class GraphMaker:
    def __init__(self, dirigido, debug=None):
        self.dirigido = dirigido
        self.debug    = debug
        self.edges    = {}
        self.vertices = {}

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertice(vertex)
            if self.debug == 1:
                self.debug_version()
            return "Inserido vértice: " + vertex
        return "Vértice já existe no grafo. Não inserido."

    def insert_edge(self, vertex_a, vertex_b, peso, label=None):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            if label is None:
                label = vertex_a+vertex_b
            if label not in self.edges:
                self.edges[label] = Aresta(vertex_a, vertex_b, peso)
                self.vertices[vertex_a].add_adj_vertex(vertex_b)
                self.vertices[vertex_b].add_adj_vertex(vertex_a)
                if self.debug == 1:
                    self.debug_version()
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
                        self.debug_version()
                    return "Verdadeiro. Os vértices " + vertex_a + " e " + vertex_b + " são adjacentes."
            return "Falso. Os vértices " + vertex_a + " e " + vertex_b + " não são adjacentes."
        return "Vértice não encontrado no grafo"

    def return_edge_element(self, edge):
        if edge in self.edges:
            return "Elemento armazenado na aresta " + str(edge) + " é: " + str(edge) + " e tem peso: " + str(self.edges[edge].peso)
        return "Aresta " + str(edge) + " não encontrada no grafo."

    def return_vertex_element(self, vertex):
        if vertex in self.vertices:
            return "Elemento armazenado no vértice " + str(vertex) + " é: " + str(self.vertices[vertex].name)
        return "Vértice " + str(vertex) + " não encontrado no grafo."

    def return_vertices_references_from_edge(self, edge):
        if edge in self.edges:
            e = self.edges[edge]
            if self.debug >= 1:
                self.debug_version()
            return "As referências dos vértices da aresta " + str(edge) + " são: " + str(e.origem) + ", " + str(e.destino) + "."
        return "Aresta " + str(edge) + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        if self.dirigido:
            gv = Digraph('G', filename='graph.gv', format='png')
        else:
            gv = Graph('G', filename='graph.gv', format='png')
        for v in self.vertices:
            gv.node(self.vertices[v].name, style='filled', fillcolor=str(self.vertices[v].color))
        for e in self.edges:
            gv.edge(self.edges[e].origem, self.edges[e].destino, label=e + " " + str(self.edges[e].peso))
        # gv.view()            # render, save and show graph image
        gv.render(view=False)  # just render and save graph image

    def debug_version(self):
        print("Dict vertices: " + str(self.vertices))
        print("Dict edges: " + str(self.edges))
        for i in self.vertices:
            print("Vertice: " + i +
                  "   Adjs: " + str(self.vertices[i].adj) +
                  "   Cor Atual: " + str(self.vertices[i].color))
        print()

    # todo: algoritmos
    def check_planar_graph(self):
        return "vitor"

    def breadth_search(self, vertex, evt):
        self.clear()
        aux = [self.vertices[vertex].name]
        self.vertices[vertex].color = 'blue'
        while 0 != len(aux):
            u = aux[0]
            v = self.get_adjacente(u)
            if v is None:
                aux.pop(0)
            else:
                self.vertices[v].color = 'blue'
                aux.append(v)
            self.vertices[u].color = 'blue'
            time.sleep(1)
            if self.debug == 2:
                print(aux)
                self.debug_version()
        message = "Vértices acessados: "
        for i in self.vertices:
             message += self.vertices[i].color
        return message

    def call_depth_search(self, vertex):
        self.clear()
        if self.debug == 2:
            self.debug_version()
        return self.depth_search(vertex)

    def depth_search(self, vertex):
        self.vertices[vertex].color = 'red'
        for i in self.vertices[vertex].adj:
            if self.vertices[i].color == 'white':
                self.depth_search(self.vertices[i].name)
        self.vertices[vertex].color = 'blue'
        if self.debug == 2:
            self.debug_version()
        return "Busca em profundidade em execução. Saída no console."

    # TODO
    def prim(self, reference):
        aux = []
        for i in self.nodos:
            aux.append(i)
        aux.sort()

        while len(aux) != 0:
            u = aux[0]
            v = self.get_adjacente(u)

            if v is None:
                for i in aux:
                    self.color[i] = 'white'
                aux.sort()
                aux.remove(u)
            else:
                w = self.get_arestas(u, v)
                print(w)
                if aux.count(v) > 0:
                    print("TESTE")
        return "vitor"

    def get_adjacente(self, u):
        for i in self.vertices[u].adj:
            if self.vertices[i].color == 'white':
                return self.vertices[i].name
        else:
            return None

    def clear(self):
        for i in self.vertices:
            self.vertices[i].color = 'white'

    # TODO
    def get_arestas(self, u, v):
        for i in self.edges:
            if u == self.edges[i][0]:
                if v == self.edges[i][1]:
                    return self.edges[i][1]
                return self.edges[i][0]
        else:
            return None