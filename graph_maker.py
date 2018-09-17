from graphviz import Graph


class GraphMaker:
    def __init__(self, debug=None):
        self.debug    = debug
        self.nodos    = []
        self.adjlist  = {}
        self.labels   = []
        self.edges    = {}
        self.color    = {}  #Usado para Depth Search e quando insere vertex coloca como preto

    def insert_vertex(self, vertex):
        if vertex not in self.nodos:
            self.nodos.append(vertex)
            self.color[vertex] = 'Black'
            self.adjlist[vertex] = []
            if self.debug >= 1:
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
                if self.debug >= 1:
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
                if self.debug >= 1:
                    print(self.nodos)
                    print(self.adjlist)
                    print(self.labels)
                    print(self.edges)
            message = "Vértice " + str(reference) + " removido.\nAtenção: referências dos vértices atualizadas."
            for i in range(0, len(self.nodos)):
                message = message + "\n" + self.return_vertex_element(i)
            return message
        return "Vértice não encontrado no grafo."

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
        if vertex_a in self.nodos and vertex_b in self.nodos:
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
            if self.debug >= 1:
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
        # gv.view()           # render, save and show graph image
        gv.render(view=False) # just render and save graph image

    # todo: algoritmos
    def check_planar_graph(self):
        return "vitor"

    def breadth_search(self, reference):
        aux = [self.nodos[reference]]
        self.color[self.nodos[reference]] = 'Blue'
        while 0 != len(aux):
            u = aux[0]
            v = self.getAdjacente(u)
            if v is None:
                aux.pop(0)
            else:
                self.color[v] = 'Blue'
                aux.append(v)
        return "Vértices acessados: " + str(self.color)

    def depth_search(self, reference):
        message = ""
        print(reference)
        self.color[self.nodos[reference]] = 'Red'
        for i in self.adjlist[self.nodos[reference]]:
            if self.color[i] == 'Black':
                self.depth_search(self.nodos.index(i))
        self.color[self.nodos[reference]] = 'Blue'
        message += message + "Vértices sendo acessados: (referência) - " + str(reference) + " : " + str(self.color)
        print(message)
        return message

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
        for i in self.adjlist[u]:
            if self.color[i] == 'Black':
                return i
        else:
            return None

    def getArestas(self, u, v):
        for i in self.edges:
            if u == self.edges[i][0]:
                if v == self.edges[i][1]:
                    return self.edges[i][1]
                return self.edges[i][0]
        else:
            return None