from graphviz import Graph
from graphviz import Digraph
from vertice import Vertice
from aresta import Aresta

from random import sample, shuffle, randrange, choice
import random

import time

SPEED = 1


class GraphMaker:
    def __init__(self, evt, directed, debug=None):
        self.directed = directed
        self.debug = debug
        self.evt = evt
        self.edges = {}
        self.vertices = {}
        self.label_type = 1

    def on_change_directed_status(self, evt):
        self.clear_vertex()
        self.clear_edges()
        if self.directed:
            self.directed = False
        else:
            self.directed = True
        return self.directed

    def insert_vertex(self, vertex, pos=None):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertice(vertex, pos)
            if self.debug >= 1:
                self.debug_version()
            return "Inserido vértice: " + vertex
        return "Vértice já existe no grafo. Não inserido."

    def insert_edge(self, vertex_a, vertex_b, peso, label=None):
        if vertex_a in self.vertices and vertex_b in self.vertices:
            if label is None or label == "":
                label = vertex_a + vertex_b
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
            return "As referências dos vértices da aresta " + str(edge) \
                   + " são: " + str(e.origem) \
                   + ", " + str(e.destino) + "."
        return "Aresta " + str(edge) + " não encontrada no grafo."

    def draw_graph(self):
        # draw graph using graphviz lib
        if self.directed:
            self.gv = Digraph('G', filename='graph.gv', format='png')
        else:
            self.gv = Graph('G', filename='graph.gv', format='png')
        for v in self.vertices:
            self.gv.node(self.vertices[v].name, style='filled', fillcolor=str(self.vertices[v].color))
        for e in self.edges:
            # APRESENTAR NOME E PESO
            if self.label_type == 2:
                self.gv.edge(self.edges[e].origem, self.edges[e].destino, label=e + " " + str(self.edges[e].peso),
                             style='filled', color=str(self.edges[e].color))
            # APRESENTAR APENAS PESO
            elif self.label_type == 1:
                self.gv.edge(self.edges[e].origem, self.edges[e].destino, str(self.edges[e].peso),
                             style='filled', color=str(self.edges[e].color))
            # APRESENTAR APENAS NOME
            elif self.label_type == 0:
                self.gv.edge(self.edges[e].origem, self.edges[e].destino, e,
                             style='filled', color=str(self.edges[e].color))
        # gv.view()            # render, save and show graph image
        self.gv.render(view=False)  # just render and save graph image

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
                          "  Estimativa: " + str(self.vertices[i].estimativa) +
                          "  Position: " + str(self.vertices[i].position))
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
        return "GREEDY COLORING DONE"

    def floyd(self):
        self.clear_estimativa()
        self.clear_edges()
        self.clear_vertex()
        matrixEst = self.createStarterMatrix()
        matrixPredec = self.createPredecMatrix()
        self.printMatrix(matrixEst, 'MATRIZ ESTIMATIVA - ITERACAO 0')
        self.printMatrix(matrixPredec, 'MATRIZ PREDECESSOR - ITERACAO 0')
        size = range(len(matrixEst))
        for k in size:
            for i in size:
                for j in size:
                    if matrixEst[i][k] + matrixEst[k][j] < matrixEst[i][j]:
                        matrixEst[i][j] = matrixEst[i][k] + matrixEst[k][j]
                        matrixPredec[i][j] = matrixPredec[k][j]
            self.printMatrix(matrixEst, 'MATRIZ ESTIMATIVA - ITERACAO ' + str(k + 1))
            self.printMatrix(matrixPredec, 'MATRIZ PREDECESSOR - ITERACAO ' + str(k + 1))
        return "FLOYD DONE"

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

    def call_a_star(self, origin, destiny, evt):
        message = ""
        self.clear_graph()
        self.evt.on_draw_graph(evt)
        self.label_type = 0
        message += self.set_graph()
        self.evt.on_draw_graph(evt)
        message += self.a_star(origin, destiny, evt)
        return message

    def a_star(self, origin, destiny, evt):
        abertos = []
        fechados = []
        path = []

        print('org', origin)
        print('dst', destiny)
        print()

        # n = 4
        # k = 0

        pai = origin
        while pai != destiny:
            print('pai', pai)
            print('filhos:')
            # self.vertices[pai].color = 'red'
            for filho in self.vertices[pai].adj:
                if filho not in abertos and filho not in fechados:
                    print(filho)
                    path.append((filho, pai))
                    # self.vertices[filho].color = 'cyan'
                    abertos.append(filho)
            print('abertos:')
            distancias = []
            for i in abertos:
                print(self.vertices[i].name, self.vertices[i].position)
                p1 = self.vertices[origin].position
                p2 = self.vertices[i].position
                p3 = self.vertices[destiny].position
                g = self.manhattan(p1, p2)  # g = custo do nodo inicial até o nodo atual
                h = self.manhattan(p2, p3)  # h = custo do nodo atual ate o nodo destino
                f = self.f(g, h)  # f = custo total
                distancias.append((self.vertices[i].name, f))
            print('distancias antes', distancias)
            distancias.sort(key=lambda tup: tup[1])
            print('distancias depois', distancias)
            fechados.append(pai)
            print('fechados:')
            for i in fechados:
                print(i)
            pai = distancias[0][0]  # list of tuples [(vertex, distance)]
            print('novo pai', pai)
            if pai in abertos:
                abertos.remove(pai)
            print('abertos restantes:')
            for i in abertos:
                print(i)
            # k += 1
            # if k == n:
            #     exit(0)
            # if self.debug >= 3:
            #     time.sleep(SPEED)
            # self.debug_version()
            # self.evt.on_draw_graph(evt)

        print('achou destino:', pai)
        predecessores = [destiny]
        node = destiny
        while node != origin:
            for i in path:
                if i[0] == node:
                    predecessores.append(i[1])
                    node = i[1]
        predecessores.reverse()
        caminho = ""
        arestas = ""
        for i in range(0, len(predecessores) - 1):
            caminho = caminho + predecessores[i] + '->'
            arestas = arestas + predecessores[i] + predecessores[i + 1] + ','
        caminho = caminho + predecessores[-1]
        distancia = self.manhattan(self.vertices[caminho[0]].position, self.vertices[caminho[-1]].position)
        print('caminho: ', caminho)
        print('distancia: ', distancia)
        print('arestas: ', arestas)
        e = arestas.split(',')
        for i in e[:len(e) - 1]:
            self.edges[i].color = 'green'
        self.evt.on_draw_graph(evt)
        return 'caminho = ' + caminho + "\ndistância (KM) = " + str(distancia) + "\nA* DONE"

    def manhattan(self, p1, p2):
        return sum([abs(p1[i] - p2[i]) for i in range(len(p1))]) / len(p1)

    def f(self, g, h):
        return g + h

    def clear_graph(self):
        self.vertices.clear()
        self.edges.clear()

    def set_graph(self):
        message = "Criando o Grafo do A*\n"
        message = message + self.set_vertices()
        message = message + self.set_edges()
        message += "Grafo do A* Inserido\n"
        return message

    def set_vertices(self):
        nodes = {'A': (950, 231),
                 'B': (607, 486),
                 'C': (891, 762),
                 'D': (456, 19),
                 'E': (821, 445),
                 'F': (615, 792),
                 'G': (922, 738),
                 'H': (176, 406),
                 'I': (935, 917),
                 'J': (410, 894),
                 'K': (58, 353),
                 'L': (813, 10),
                 'M': (139, 203),
                 'N': (199, 604),
                 'O': (272, 199),
                 'P': (15, 747),
                 'Q': (445, 932),
                 'R': (466, 419),
                 'S': (846, 525),
                 'T': (203, 672)}

        message = ""
        for i in nodes:
            # print(i, nodes[i])
            message = message + self.insert_vertex(i, nodes[i]) + '\n'
        return message

    def set_edges(self):
        edges = ('A,B', 'A,E', 'A,G', 'A,L', 'A,S',
                 'B,A', 'B,E', 'B,F', 'B,J', 'B,R', 'B,S', 'B,T',
                 'C,F', 'C,G', 'C,I',
                 'D,L', 'D,M', 'D,R',
                 'E,A', 'E,B',
                 'F,J', 'F,B', 'F,S', 'F,C',
                 'G,I', 'G,C', 'G,S', 'G,A',
                 'H,N', 'H,O', 'H,P',
                 'I,Q', 'I,C', 'I,G',
                 'J,P', 'J,Q', 'J,T', 'J,B', 'J,F',
                 'K,M', 'K,P',
                 'L,R', 'L,A', 'L,D',
                 'M,D', 'M,K', 'M,O',
                 'N,P', 'N,R', 'N,T', 'N,H',
                 'O,R', 'O,M', 'O,H',
                 'P,T', 'P,N', 'P,H', 'P,K', 'P,J',
                 'Q,I', 'Q,J',
                 'R,N', 'R,O', 'R,D', 'R,L', 'R,B',
                 'S,F', 'S,B', 'S,G', 'S,A',
                 'T,P', 'T,J', 'T,B')

        message = ""
        for i in edges:
            vertex_a, vertex_b = i.split(',')
            message = message + self.insert_edge(vertex_a, vertex_b, "") + '\n'
        return message

    def call_tsp(self, population, crossover, mutation, generation, evt):
        message = ""
        self.clear_graph()
        self.evt.on_draw_graph(evt)
        message += self.set_map()
        self.evt.on_draw_graph(evt)
        message += self.tsp(population, crossover, mutation, generation, evt)
        return message

    def tsp(self, population_size, crossover, mutation, generation, evt):

        population = self.generate_first_population(population_size)
        print('antes do crossover')
        for ind in population:
            print(ind)
        population = self.crossover(population, crossover)
        print('depois do crossover')
        for ind in population:
            print(ind)

        # print('antes da mutação')
        # for ind in population:
        #     print(ind)
        population = self.make_mutation(population, mutation)
        # print('depois da mutação')
        # for ind in population:
        #     print(ind)

        return 'O menu vale 0.63?!?! :)'

    def set_map(self):
        message = "Criando o Mapa do Problema do Caixeiro Viajante\n"
        message = message + self.set_cities()
        message = message + self.set_routes()
        message += "Mapa do Problema do Caixeiro Viajante Inserido\n"
        return message

    def set_cities(self):
        nodes = (
            "E",
            "F",
            "G",
            "H",
            "K",
            "L",
            "N"
        )
        message = ""
        for vertex in nodes:
            message = message + self.insert_vertex(vertex) + "\n"
        return message

    def set_routes(self):
        edges = ('E,F,10', 'E,G,40', 'E,H,60', 'E,K,10', 'E,L,5',
                 'F,N,47', 'F,L,10', 'F,H,30', 'F,E,10', 'F,K,70',
                 'G,K,90', 'G,E,40', 'G,H,80',
                 'H,L,40', 'H,F,30', 'H,K,73', 'H,E,60', 'H,G,80',
                 'K,N,60', 'K,F,70', 'K,H,73', 'K,E,10', 'K,G,90',
                 'L,H,40', 'L,E,5', 'L,F,10',
                 'N,F,47', 'N,K,60')

        message = ""
        for i in edges:
            vertex_a, vertex_b, weight = i.split(',')
            message = message + self.insert_edge(vertex_a, vertex_b, weight) + '\n'
        return message

    def generate_first_population(self, population_size):
        enunciado = False
        if enunciado:
            population = []
            print("Criando a população inicial...")
            f = open("population.csv", 'w')
            while len(population) < population_size:
                print("Criando individuo...")
                individuo = [(choice(list(self.vertices)))]
                rotas = self.vertices[individuo[-1]].adj
                while len(individuo) < len(self.vertices):
                    # print("Gerando rota...")
                    rota = choice(rotas)
                    if rota not in individuo:
                        individuo.append(rota)
                        rotas = self.vertices[individuo[-1]].adj
                        if len(individuo) == len(self.vertices):
                            while individuo[0] not in rotas:
                                print("Nao passa por todas as cidades... Voltando")
                                individuo.pop()
                                rotas = self.vertices[individuo[-1]].adj
                print("Individuo criado")
                # print(individuo)
                f.write(
                    individuo[0] + ',' +
                    individuo[1] + ',' +
                    individuo[2] + ',' +
                    individuo[3] + ',' +
                    individuo[4] + ',' +
                    individuo[5] + ',' +
                    individuo[6] + '\n')
                population.append(individuo)
            print("População criada...")
            # print(population)
            return population
        else:
            print("Criando a população inicial...")
            population = self.shuffle_first_population(population_size)
            print("População criada...")
            # for ind in population:
            #     print(ind)
            return population

    def shuffle_first_population(self, population_size):
        population = []
        l = []
        for v in self.vertices:
            l.append(v)
        while len(population) < population_size:
            shuffle(l)
            population.append(list(l))
        return population

    def crossover(self, population, crossover_rate):
        newPopulation = []
        for index in range(0, len(population)):
            if index < crossover_rate:
                firstParent = population[random.randint(1, len(population)-1)]
                secondParent = population[random.randint(1, len(population)-1)]
                newSon = []
                randChoice = random.randint(1, len(firstParent))
                for i in range(len(firstParent)):
                    if i <= randChoice:
                        newSon.append(firstParent[i])
                    else:
                        newSon.append(secondParent[i])
                newPopulation.append(newSon)
            else:
                newPopulation.append(population[random.randint(1, len(population)-1)])
        return newPopulation


    def mutate(self, individual, mutation_rate):
        for swapped in range(len(individual)):
            if random.random() < mutation_rate:
                swap_with = int(random.random() * len(individual))

                city1 = individual[swapped]
                city2 = individual[swap_with]

                individual[swapped] = city2
                individual[swap_with] = city1

        return individual

    def make_mutation(self, population, mutation_rate):
        mutated_pop = []

        for ind in range(0, len(population)):
            mutated_ind = self.mutate(population[ind], mutation_rate)
            mutated_pop.append(mutated_ind)
        return mutated_pop

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
            if self.directed:
                if origem == u and destino == v:
                    return i
            else:
                if origem == u and destino == v or origem == v and destino == u:
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

    def createStarterMatrix(self):
        matriz = []
        for i in self.vertices:
            linha = []
            for j in self.vertices:
                if i == j:
                    linha.append(0)
                elif self.check_adj(i, j):
                    if self.vertices[i].name + self.vertices[j].name in self.edges:
                        linha.append(self.edges[self.vertices[i].name + self.vertices[j].name].peso)
                    else:
                        linha.append(self.edges[self.vertices[j].name + self.vertices[i].name].peso)
                else:
                    linha.append(9999)
            matriz.append(linha)
        return matriz

    def createPredecMatrix(self):
        matriz = []
        for i in self.vertices:
            linha = []
            for j in self.vertices:
                if i == j:
                    linha.append(0)
                else:
                    linha.append(i)
            matriz.append(linha)
        return matriz

    def check_adj(self, u, v):
        if v in self.vertices[u].adj:
            if self.directed:
                if self.vertices[u].name + self.vertices[v].name in self.edges:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def printMatrix(self, matrix, text):
        print('\n\n' + text)
        for i in range(len(matrix)):
            print(str(i) + ' - ', end='')
            for j in matrix[i]:
                print(str(j) + ' ', end='')
            print()
