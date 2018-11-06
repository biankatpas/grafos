from graphviz import Graph
from graphviz import Digraph
from vertice import Vertice
from aresta import Aresta
import time

SPEED = 1


class GraphMaker:
    def __init__(self, evt, directed, debug=None):
        self.directed = directed
        self.debug = debug
        self.evt = evt
        self.edges = {}
        self.vertices = {}

    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertice(vertex)
            if self.debug >= 1:
                self.debug_version()
            return "Inserido vértice: " + vertex
        return "Vértice já existe no grafo. Não inserido."

    def insert_edge(self, vertex_a, vertex_b, peso, label=None):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            if label is None or label == "":
                label = vertex_a+vertex_b
            if label not in self.edges:
                if peso != "":
                    self.edges[label] = Aresta(vertex_a, vertex_b, peso)
                else:
                    self.edges[label] = Aresta(vertex_a, vertex_b)
                self.vertices[vertex_a].add_adj_vertex(vertex_b)
                self.vertices[vertex_b].add_adj_vertex(vertex_a)
                if self.debug >= 1:
                    self.debug_version()
                return "Inserida aresta: " + label
            return "Aresta já existe no grafo. Não inserida."
        return "Inserir os vértices primeiro."

    def remove_vertex(self, vertex):
        if vertex not in self.vertices:
            return "Vértice não encontrado no grafo."
        else:
            self.vertices.pop(vertex)
            for i in self.vertices:
                if vertex in self.vertices[i].adj:
                    self.vertices[i].delete_adj_vertex(vertex)
            delete = []
            for i in self.edges:
                if self.edges[i].origem == vertex or self.edges[i].destino == vertex:
                    delete.append(i)
            for d in delete:
                self.edges.pop(d)
            return "Vértice " + vertex + " removido."

    def remove_edge(self, reference):
        if reference in self.edges:
            a = self.edges[reference].origem
            b = self.edges[reference].destino
            self.edges.pop(reference)
            self.vertices[a].delete_adj_vertex(b)
            self.vertices[b].delete_adj_vertex(a)
            return "Aresta " + str(reference) + " removida."
        else:
            return "Aresta " + str(reference) + " não encontrada no grafo."

    def check_adjacency(self, vertex_a, vertex_b):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            for i in self.edges:
                origem = self.edges[i].origem
                destino = self.edges[i].destino
                if vertex_a == origem and vertex_b == destino or vertex_a == destino and vertex_b == origem:
                    if self.debug >= 2:
                        self.debug_version()
                    return "Verdadeiro. Os vértices " + vertex_a + " e " + vertex_b + " são adjacentes."
            return "Falso. Os vértices " + vertex_a + " e " + vertex_b + " não são adjacentes."
        return "Vértice não encontrado no grafo"

    def return_edge_element(self, edge):
        if edge in self.edges:
            return "Elemento armazenado na aresta " + str(edge) + \
                   " é: " + str(edge) + \
                   " e tem peso: " + str(self.edges[edge].peso)
        return "Aresta " + str(edge) + " não encontrada no grafo."

    def return_vertex_element(self, vertex):
        if vertex in self.vertices:
            return "Elemento armazenado no vértice " + str(vertex) + " é: " + str(self.vertices[vertex].name)
        return "Vértice " + str(vertex) + " não encontrado no grafo."

    def return_vertices_references_from_edge(self, edge):
        if edge in self.edges:
            e = self.edges[edge]
            if self.debug >= 2:
                self.debug_version()
            return "As referências dos vértices da aresta " + str(edge)\
                   + " são: " + str(e.origem)\
                   + ", " + str(e.destino) + "."
        return "Aresta " + str(edge) + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        if self.directed:
            gv = Digraph('G', filename='graph.gv', format='png')
        else:
            gv = Graph('G', filename='graph.gv', format='png')
        for v in self.vertices:
            gv.node(self.vertices[v].name, style='filled', fillcolor=str(self.vertices[v].color))
        for e in self.edges:
            # APRESENTAR NOME E PESO
            # gv.edge(self.edges[e].origem, self.edges[e].destino, label=e + " " + str(self.edges[e].peso),
            #         style='filled', color=str(self.edges[e].color))
            # APRESENTAR APENAS PESO
            gv.edge(self.edges[e].origem, self.edges[e].destino, str(self.edges[e].peso),
                    style='filled', color=str(self.edges[e].color))
        # gv.view()            # render, save and show graph image
        gv.render(view=False)  # just render and save graph image

    def debug_version(self):
        print("Dict vertices: " + str(self.vertices))
        print("Dict edges: " + str(self.edges))
        if self.debug >= 2:
            for i in self.vertices:
                print("Vértice: " + i +
                      "   Adjs: " + str(self.vertices[i].adj) +
                      "   Cor Atual: " + str(self.vertices[i].color))
                if self.debug >= 3:
                    print("Vértice: " + i +
                          "  Predecessor: " + str(self.vertices[i].precedente) +
                          "  Estimativa: " + str(self.vertices[i].estimativa))
        print()

    # TODO
    def check_planar_graph(self):
        return "PLANAR"

    def breadth_search(self, vertex, evt):
        self.clear_vertex()
        aux = [self.vertices[vertex].name]
        self.vertices[vertex].color = 'blue'
        while 0 != len(aux):
            u = aux[0]
            v = self.get_adjacent(u)
            if v is None:
                aux.pop(0)
            else:
                self.vertices[v].color = 'blue'
                aux.append(v)
            self.vertices[u].color = 'blue'
            time.sleep(SPEED)
            if self.debug >= 2:
                print(aux)
                self.debug_version()
                self.evt.on_draw_graph(evt)
        message = "Vértices acessados: "
        for i in self.vertices:
             message += self.vertices[i].color
        return message

    def call_depth_search(self, vertex, evt):
        self.clear_vertex()
        if self.debug >= 2:
            self.debug_version()
        return self.depth_search(vertex, evt)

    def depth_search(self, vertex, evt):
        self.vertices[vertex].color = 'red'
        for i in self.vertices[vertex].adj:
            if self.vertices[i].color == 'white':
                self.depth_search(self.vertices[i].name, evt)
        self.vertices[vertex].color = 'blue'
        if self.debug >= 2:
            time.sleep(SPEED)
            self.debug_version()
            self.evt.on_draw_graph(evt)
        return "Busca em profundidade em execução. Saída no console."

    # TODO
    def prim(self, reference):
        return "PRIM"

    def greed_coloring(self, evt):
        self.clear_vertex()
        high_degree = self.get_higher_degree()
        colours = ['blue', 'red', 'cyan', 'gold', 'green', 'violet', 'tan', 'pink3']
        aux = [high_degree]
        self.vertices[high_degree].color = colours[0]
        while 0 != len(aux):
            u = aux[0]
            for i in self.vertices[u].adj:
                if self.vertices[i].name not in aux:
                    if self.vertices[i].color == 'white':
                        aux.append(self.vertices[i].name)
            if self.vertices[u].color != 'white':
                aux.pop(0)
            else:
                for i in colours:
                    cont = len(self.vertices[u].adj)
                    for j in self.vertices[u].adj:
                        if self.vertices[j].color == i:
                            break
                        cont -= 1
                    if cont == 0:
                        self.vertices[u].color = i
                        aux.pop(0)
                        if self.debug >= 2:
                            time.sleep(SPEED)
                            self.debug_version()
                            self.evt.on_draw_graph(evt)
                        break
        return "Done Greedy Coloring"

    # TODO
    def floyd(self):
        return "FLOYD"

    def dijkstra(self, vertex, evt):
        self.clear_estimativa()
        self.clear_edges()
        self.clear_vertex()
        open_vertex = []
        color_to_reset = []
        self.vertices[vertex].estimativa = 0
        self.vertices[vertex].precedente = vertex
        for i in self.vertices:
            open_vertex.append(i)
        while len(open_vertex) != 0:
            open_vertex = self.sort_dict(open_vertex)
            self.vertices[open_vertex[0]].color = 'red'
            u = open_vertex[0]
            v = self.get_adjacent(u)
            if v is None:
                for i in color_to_reset:
                    self.vertices[i].color = 'white'
                color_to_reset.clear()
                open_vertex.pop(0)
            else:
                w = self.get_edge(u, v)
                peso_test = self.vertices[u].estimativa + self.edges[w].peso
                if self.vertices[v].estimativa <= peso_test:
                    self.vertices[v].estimativa = self.edges[w].peso
                else:
                    self.vertices[v].estimativa = peso_test
                self.vertices[v].precedente = self.vertices[u].name
                self.vertices[v].color = 'blue'
                color_to_reset.append(v)
            if self.debug >= 3:
                time.sleep(SPEED)
                self.debug_version()
                self.evt.on_draw_graph(evt)
        time.sleep(SPEED * 2)
        self.set_color_on_edges(evt)
        return "DIJKSTRA DONE"

    def get_adjacent(self, u):
        for i in self.vertices[u].adj:
            if self.vertices[i].color == 'white':
                if self.directed:
                    edge = self.vertices[u].name + self.vertices[i].name
                    if edge in self.edges:
                        return self.vertices[i].name
                else:
                    return self.vertices[i].name
        else:
            return None

    def clear_vertex(self, color='white'):
        for i in self.vertices:
            self.vertices[i].color = color

    def clear_edges(self, color='black'):
        for e in self.edges:
            self.edges[e].color = color

    def clear_estimativa(self):
        for i in self.vertices:
            self.vertices[i].estimativa = 9999

    def get_higher_degree(self):
        high = 0
        vertex = 'A'
        for i in self.vertices:
            if len(self.vertices[i].adj) >= high:
                high = len(self.vertices[i].adj)
                vertex = self.vertices[i].name
        return self.vertices[vertex].name

    def get_edge(self, u, v):
        for i in self.edges:
            origem = self.edges[i].origem
            destino = self.edges[i].destino
            if origem == u and destino == v:
                return i

    def sort_dict(self, vet):
        sorted_vet = []
        for i in vet:
            sorted_vet.append(self.vertices[i])
        sorted_vet.sort()
        vet.clear()
        for i in sorted_vet:
            vet.append(i.name)
        return vet

    def set_color_on_edges(self, evt, color='green'):
        for i in self.vertices:
            self.vertices[i].color = 'cyan'
            predecessor = self.vertices[i].precedente
            if predecessor != self.vertices[i].name:
                self.edges[predecessor + self.vertices[i].name].color = color
        self.evt.on_draw_graph(evt)
