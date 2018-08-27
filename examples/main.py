from grafoMaker import GrafoMaker
from graphviz import Graph


grafo = Graph ('G', filename='testing.gv')

g = GrafoMaker()

numero1 = g.insertVertex("A", grafo)
numero2 = g.insertVertex("B", grafo)
numero3 = g.insertEdge("A", "B", "AB", grafo)

print(numero1, numero2, numero3)

grafo.view()