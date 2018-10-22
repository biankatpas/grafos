import os
from gui import Gui
from event_handler import EventHandler


DEBUG = 50
# 1 - Apresentar Dict vertices e edges
# 2 - Apresentar Adjs e cor
# 3 - Apresentar Predecessor e Estimativa
# 50 - Auto colocar vertices

if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

W_SIZE = 1080
H_SIZE = 720
g = Gui(None, title="Trb M1 - Grafos", size=(W_SIZE, H_SIZE))
e = EventHandler(g, DEBUG)

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
            "PRIM",
            "Coloração gulosa",
            "Floyd",
            "Dijkstra"
         )

g.add_button(labels[0], (0, (h * len(g.get_buttons()))), callback=e.on_insert_vertex)
g.add_button(labels[1], (0, (h * len(g.get_buttons()))), callback=e.on_insert_edge)
g.add_button(labels[2], (0, (h * len(g.get_buttons()))), callback=e.on_remove_vertex)
g.add_button(labels[3], (0, (h * len(g.get_buttons()))), callback=e.on_remove_edge)
g.add_button(labels[4], (0, (h * len(g.get_buttons()))), callback=e.on_check_adjacency)
# g.add_button(labels[5], (0, (h * len(g.get_buttons()))), callback=e.on_return_edge_element)
# g.add_button(labels[6], (0, (h * len(g.get_buttons()))), callback=e.on_return_vertex_element)
# g.add_button(labels[7], (0, (h * len(g.get_buttons()))), callback=e.on_return_vertices_references_from_edge)
# g.add_button(labels[8], (0, (h * len(g.get_buttons()))), callback=e.on_check_planar_graph)
g.add_button(labels[9], (0, (h * len(g.get_buttons()))), callback=e.on_breadth_search)
g.add_button(labels[10], (0, (h * len(g.get_buttons()))), callback=e.on_depth_search)
# g.add_button(labels[11], (0, (h * len(g.get_buttons()))), callback=e.on_prim)
g.add_button(labels[12], (0, (h * len(g.get_buttons()))), callback=e.on_greed_coloring)
g.add_button(labels[13], (0, (h * len(g.get_buttons()))), callback=e.on_floyd)
g.add_button(labels[14], (0, (h * len(g.get_buttons()))), callback=e.on_dijkstra)

g.Show()
g.main_loop()
