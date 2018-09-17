import wx
from graphviz import Graph


class GraphMaker:
    def __init__(self, gui, debug=None):
        self.debug    = debug
        self.gui      = gui
        self.nodes    = []  # aux
        self.adjlist  = {}  # dict de adjs
        self.weights  = []  # aux
        self.edges    = {}  # dict de arestas
        self.color    = {}  # Usado para Depth Search e quando insere o vertex coloca como preto
        self.message  = ""  # Usado para retornar msg no metodo recursivo (Depth Search)

    def insert_vertex(self, vertex):
        if vertex not in self.nodes:
            self.nodes.append(vertex)
            self.color[vertex] = 'Black'
            self.adjlist[vertex] = []
            if self.debug >= 1:
                print(self.adjlist)
            return "Inserido vértice: " + vertex + ". Referência: " + str(self.nodes.index(vertex))
        return "Vértice já existe no grafo. Não inserido."


    def insert_edge(self, vertex_a, vertex_b, label=None):
        if vertex_a in self.nodes and vertex_b in self.nodes:
            if label is None:
                label = vertex_a+vertex_b
            if label not in self.weights:
                self.weights.append(label)
                self.edges[label] = [vertex_a, vertex_b]
                self.adjlist[vertex_a].append(vertex_b)
                self.adjlist[vertex_b].append(vertex_a)
                if self.debug >= 1:
                    print(self.adjlist)
                    print(self.edges)
                return "Inserida aresta: " + label + ". Referência: " + str(self.weights.index(label))
            return "Aresta já existe no grafo. Não inserida."
        return "Inserir os vértices primeiro."

    def remove_vertex(self, reference):
        if reference < len(self.nodes):
            vertex = self.nodes[reference]
            self.nodes.pop(reference)
            self.color.pop(vertex)
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
                self.weights.remove(d)
                self.edges.pop(d)
                if self.debug >= 1:
                    print(self.nodes)
                    print(self.adjlist)
                    print(self.weights)
                    print(self.edges)
            message = "Vértice " + str(reference) + " removido.\nAtenção: referências dos vértices atualizadas."
            for i in range(0, len(self.nodes)):
                message = message + "\n" + self.return_vertex_element(i)
            return message
        return "Vértice não encontrado no grafo."

    def remove_edge(self, reference):
        if reference < len(self.weights):
            e = self.weights[reference]
            self.weights.pop(reference)
            self.edges.pop(e)
            if self.debug >= 1:
                print(self.weights)
                print(self.edges)
            message = "Aresta " + str(reference) + " removida.\nAtenção: referências das arestas atualizadas."
            for i in range(0, len(self.weights)):
                message = message + "\n" + self.return_edge_element(i)
            return message
        return "Aresta " + str(reference) + " não encontrada no grafo."

    def check_adjacency(self, vertex_a, vertex_b):
        if vertex_a in self.nodes and vertex_b in self.nodes:
            adj_a = self.adjlist[vertex_a]
            adj_b = self.adjlist[vertex_b]
            if vertex_a in adj_b and vertex_b in adj_a:
                if self.debug >= 1:
                    print(adj_a)
                    print(adj_b)
                return "Verdadeiro. Os vértices " + vertex_a + " e " + vertex_b + " são adjacentes."
            return "Falso. Os vértices " + vertex_a + " e " + vertex_b + " não são adjacentes."
        return "Vértice não encontrado no grafo"

    def return_edge_element(self, reference):
        if reference < len(self.weights):
            return "Elemento armazenado na aresta " + str(reference) + " é: " + self.weights[reference]
        return "Aresta " + str(reference) + " não encontrada no grafo."

    def return_vertex_element(self, reference):
        if reference < len(self.nodes):
            return "Elemento armazenado no vértice " + str(reference) + " é: " + self.nodes[reference]
        return "Vértice " + str(reference) + " não encontrado no grafo."

    def return_vertices_references_from_edge(self, reference):
        if reference < len(self.weights):
            e = self.weights[reference]
            vertices = self.edges[e]
            vertex_a = self.nodes.index(vertices[0])
            vertex_b = self.nodes.index(vertices[1])
            if self.debug >= 1:
                print(e)
                print(vertices)
            return "As referências dos vértices da aresta " + str(reference) + " são: " + str(vertex_a) + "," + str(vertex_b) + "."
        return "Aresta " + str(reference) + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        gv = Graph('G', filename='graph.gv', format='png')
        for nodo in self.nodes:
            gv.node(nodo)
        for e in self.edges:
            gv.edge(self.edges[e][0], self.edges[e][1], label=e)
        # gv.view()           # render, save and show graph image
        gv.render(view=False) # just render and save graph image

    # todo
    def check_planar_graph(self):
        return "to-do"

    def breadth_search(self, reference):
        # self.clear()
        aux = [self.nodes[reference]]
        self.color[self.nodes[reference]] = 'Blue'
        while 0 != len(aux):
            u = aux[0]
            v = self.get_adjacent(u)
            if v is None:
                aux.pop(0)
            else:
                self.color[v] = 'Blue'
                print(self.color)
                aux.append(v)
        # return "Vértices acessados: " + str(self.color)
        return "Busca em largura em execução. Saída no console."
    # todo: conferir a msg de saída
    def clear(self):
        for i in range(0, (len(self.color))):
            self.color[i] = 'Black'
        self.message = ""

    def call_depth_search(self, reference):
        # self.clear()
        return self.depth_search(reference)

    def depth_search(self, reference):
        # print('reference',str(reference))
        self.color[self.nodes[reference]] = 'Red'
        for i in self.adjlist[self.nodes[reference]]:
            if self.color[i] == 'Black':
                self.depth_search(self.nodes.index(i))
        self.color[self.nodes[reference]] = 'Blue'
        # print(self.color)
        # self.message = self.message + "Vértice sendo acessado: " + str(reference) + "\n{  "
        # message = str(reference) + "\n{  "
        # keys = [*self.color]
        # for k in keys:
            # self.message = self.message + "" + k + ": " + self.color[k] + "  "
            # message = message + "" + k + ": " + self.color[k] + "  "
        # self.message = self.message + "}\n"
        # message = message + "}\n"
        print(self.color)
        # self.gui.show_message_dialog("Vértice sendo acessado", message)
        return "Busca em profundidade em execução. Saída no console."
        # return "Busca em profundidade em execução.\n" + message

    # todo
    def prim(self, reference):
        aux = []
        for i in self.nodes:
            aux.append(i)
        aux.sort()

        while len(aux) != 0:
            u = aux[0]
            v = self.get_adjacent(u)

            if v is None:
                for i in aux:
                    self.color[i] = 'Black'
                aux.sort()
                aux.remove(u)
            else:
                w = self.get_edges(u, v)
                print(w)
                if aux.count(v) > 0:
                    print("TESTE")
        return "to-do"

    def get_adjacent(self, u):
        for i in self.adjlist[u]:
            if self.color[i] == 'Black':
                return i
        else:
            return None

    def get_edges(self, u, v):
        for i in self.edges:
            if u == self.edges[i][0]:
                if v == self.edges[i][1]:
                    return self.edges[i][1]
                return self.edges[i][0]
        else:
            return None

    def clear_message(self):
        self.message=""
