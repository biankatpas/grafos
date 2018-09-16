import os

from gui import Gui
from event_handler import EventHandler


DEBUG = 0
if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

W_SIZE = 1314
H_SIZE = 768
g = Gui(None, title="Trb M1 - Grafos", size=(W_SIZE, H_SIZE))
e = EventHandler(g)

h = 65
labels = (
            "Inserir um vértice isolado",
            "Inserir uma aresta",
            "Remover vértice",
            "Remover aresta",
            "Verificar se dois vértices sao adjacentes",
            "Retornar elemento de uma aresta",
            "Retornar elemento de um vértice",
            "Retornar referência dos vértices de uma aresta",
            "Verificar se o grafo é planar",
            "Busca em largura",
            "Busca em profundidade",
            "PRIM"
         )

g.addButton(labels[0] , (0, (h*len(g.getButtons()))), callback=e.OnInsertVertex)
g.addButton(labels[1] , (0, (h*len(g.getButtons()))), callback=e.OnInsertEdge)
g.addButton(labels[2] , (0, (h*len(g.getButtons()))), callback=e.OnRemoveVertex)
g.addButton(labels[3] , (0, (h*len(g.getButtons()))), callback=e.OnRemoveEdge)
g.addButton(labels[4] , (0, (h*len(g.getButtons()))), callback=e.OnCheck2VertexAdjacency)
g.addButton(labels[5] , (0, (h*len(g.getButtons()))), callback=e.OnReturnEdgeElement)
g.addButton(labels[6] , (0, (h*len(g.getButtons()))), callback=e.OnReturnVertexElement)
g.addButton(labels[7] , (0, (h*len(g.getButtons()))), callback=e.OnReturn2VertexReferences)
g.addButton(labels[8] , (0, (h*len(g.getButtons()))), callback=e.OnCheckPlanarGraph)
g.addButton(labels[9] , (0, (h*len(g.getButtons()))), callback=e.OnBreadthSearch)
g.addButton(labels[10], (0, (h*len(g.getButtons()))), callback=e.OnDepthSearch)
g.addButton(labels[11], (0, (h*len(g.getButtons()))), callback=e.OnPRIM)

g.renderGraph()

g.Show()
g.MainLooop()
