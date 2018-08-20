from gui import Gui
from event_handler import EventHandler


W_SIZE = 800
H_SIZE = 600
g = Gui(None, title="", size=(W_SIZE, H_SIZE))
e = EventHandler(g)

g.addButton("Inserir vértice isolado", (0, (30*len(g.getButtons()))), callback=e.onInsertVertex)
g.addButton("Inserir Aresta" , (0, (30*len(g.getButtons()))), callback=e.onInsertEdge)
g.addButton("Remover vertice" , (0, (30*len(g.getButtons()))), callback=e.onRemoveVertex)
g.addButton("Remover aresta" , (0, (30*len(g.getButtons()))), callback=e.onRemoveEdge)
g.addButton("Verificar se dois vertices sao adjacentes" , (0, (30*len(g.getButtons()))), callback=e.onCheckAdjacency)
g.addButton("Retornar elemento de uma aresta" , (0, (30*len(g.getButtons()))), callback=e.onReturnEdgeElement)
g.addButton("Retornar elemento de um vertice" , (0, (30*len(g.getButtons()))), callback=e.onReturnVertexElement)
g.addButton("Retornar referencias para dois vertices finais de aresta" , (0, (30*len(g.getButtons()))), callback=e.onReturn2VertexReferences)
g.Show()
g.MainLooop()
