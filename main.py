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

g.add_button(labels[0], (0, (h * len(g.get_buttons()))), callback=e.OnInsertVertex)
g.add_button(labels[1], (0, (h * len(g.get_buttons()))), callback=e.OnInsertEdge)
g.add_button(labels[2], (0, (h * len(g.get_buttons()))), callback=e.OnRemoveVertex)
g.add_button(labels[3], (0, (h * len(g.get_buttons()))), callback=e.OnRemoveEdge)
g.add_button(labels[4], (0, (h * len(g.get_buttons()))), callback=e.OnCheck2VertexAdjacency)
g.add_button(labels[5], (0, (h * len(g.get_buttons()))), callback=e.OnReturnEdgeElement)
g.add_button(labels[6], (0, (h * len(g.get_buttons()))), callback=e.OnReturnVertexElement)
g.add_button(labels[7], (0, (h * len(g.get_buttons()))), callback=e.OnReturnEdge2VertexReferences)
g.add_button(labels[8], (0, (h * len(g.get_buttons()))), callback=e.OnCheckPlanarGraph)
g.add_button(labels[9], (0, (h * len(g.get_buttons()))), callback=e.OnBreadthSearch)
g.add_button(labels[10], (0, (h * len(g.get_buttons()))), callback=e.OnDepthSearch)
g.add_button(labels[11], (0, (h * len(g.get_buttons()))), callback=e.OnPRIM)

# TODO: renderizar ao modificar o grafo
g.render_graph()

g.Show()
g.main_loop()
