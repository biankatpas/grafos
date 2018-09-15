from gui import Gui
from event_handler import EventHandler


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

g.addButton(labels[0] , (0, (h*len(g.getButtons()))), callback=e.onInsertVertex)
g.addButton(labels[1] , (0, (h*len(g.getButtons()))), callback=e.onInsertEdge)
g.addButton(labels[2] , (0, (h*len(g.getButtons()))), callback=e.onRemoveVertex)
g.addButton(labels[3] , (0, (h*len(g.getButtons()))), callback=e.onRemoveEdge)
g.addButton(labels[4] , (0, (h*len(g.getButtons()))), callback=e.onCheck2VertexAdjacency)
g.addButton(labels[5] , (0, (h*len(g.getButtons()))), callback=e.onReturnEdgeElement)
g.addButton(labels[6] , (0, (h*len(g.getButtons()))), callback=e.onReturnVertexElement)
g.addButton(labels[7] , (0, (h*len(g.getButtons()))), callback=e.onReturn2VertexReferences)
g.addButton(labels[8] , (0, (h*len(g.getButtons()))), callback=e.onCheckPlanarGraph)
g.addButton(labels[9] , (0, (h*len(g.getButtons()))), callback=e.onBreadthSearch)
g.addButton(labels[10], (0, (h*len(g.getButtons()))), callback=e.onDepthSearch)
g.addButton(labels[11], (0, (h*len(g.getButtons()))), callback=e.onPRIM)

g.addViewer()

g.Show()
g.MainLooop()
