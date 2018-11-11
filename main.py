import os
from gui import Gui
from event_handler import EventHandler


DEBUG = 0
# 1 - Apresentar Dict vertices e edges
# 2 - Apresentar Adjs e cor
# 3 - Apresentar Predecessor e Estimativa
# 50 - Auto colocar vertices

if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

W_SIZE = 1080
H_SIZE = 720
g = Gui(None, title="Trb M2 - Grafos", size=(W_SIZE, H_SIZE))
e = EventHandler(g, DEBUG)

g.set_evt_handler(e)
g.add_menu_bar()

g.Show()
g.main_loop()
