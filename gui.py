import wx
import wx.lib.scrolledpanel as scrolled
import numpy as np
import PIL
from PIL import Image

from event_handler import EventHandler

app = wx.App()


class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)
        self.Center()
        self.SetMaxSize(self.GetSize())
        self.SetMinSize(self.GetSize())
        self.SetBackgroundColour(colour=wx.WHITE)
        self.scrolled_panel = scrolled.ScrolledPanel(self, -1, size=(914, 650), pos=(420,0) , style=wx.SUNKEN_BORDER)
        self.scrolled_panel.SetBackgroundColour(wx.WHITE)
        self.bitmap = wx.StaticBitmap(parent=self.scrolled_panel)
        self.text_area = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE | wx.BORDER_SUNKEN | wx.TE_READONLY | wx.TE_RICH2)
        self.text_area.SetSize((400,600))
        self.text_area.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self.text_area.AppendText("Nothing have done yet!" + "\n\n")
        self.text_area.SetToolTip('Saída')
        self.hslider = wx.Slider(self, -1, 100, 100, 200, size=(394, -1), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.hslider.SetPosition((10,610))
        self.hslider.Bind(wx.EVT_SCROLL, self.on_scroll)
        self.factor = 1
        self.evt = EventHandler(self)

    def add_menu_bar(self):
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # menu itens
        self.graphMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers the same event
        self.insert_vertex = self.graphMenu.Append(-1, "&Inserir Vértice", "Insere um vértice no grafo!")
        self.insert_edge = self.graphMenu.Append(-1, "&Inserir Aresta", "Insere uma aresta no grafo!")
        self.remove_vertex = self.graphMenu.Append(-1, "&Remover Vértice", "Remove um vértice do grafo!")
        self.remove_edge = self.graphMenu.Append(-1, "&Remover Aresta", "Remove uma aresta do grafo!")
        self.check_adjacency = self.graphMenu.Append(-1, "&Verificar Adjacência", "Verificar se dois vértices são adjacentes!")
        self.return_edge_element = self.graphMenu.Append(-1, "&Retornar Elemento da Aresta", "Retorna o elemento da aresta!")
        self.return_vertex_element = self.graphMenu.Append(-1, "&Retornar Elemento do Vértice", "Retorna o elemento do vértice!")
        self.return_vertices_references_from_edge = self.graphMenu.Append(-1, "&Retornar a Referência dos Vértices da Aresta", "Retorna a referência dos dois vértices de uma aresta!")
        self.check_planar_graph = self.graphMenu.Append(-1, "&Verificar Planaridade", "Verifica se o grafo é planar!")
        self.breadth_search = self.graphMenu.Append(-1, "&Busca em Largura", "Efetua a busca em largura no grafo!")
        self.depth_search = self.graphMenu.Append(-1, "&Busca em Profundidade", "Efetua a busca em profundidade no grafo!")
        self.prim = self.graphMenu.Append(-1, "&PRIM", "Executa o algoritmo de PRIM!")
        self.graphMenu.AppendSeparator()
        self.green_coloring = self.graphMenu.Append(-1, "&Coloração Gulosa", "Executa o algorimo de coloração gulosa!")
        self.floyd = self.graphMenu.Append(-1, "&Floyd", "Executa o algorimo floyd!")
        self.dijkstra = self.graphMenu.Append(-1, "&Dijkstra", "Executa o algorimo dijkstra!")
        self.a_star = self.graphMenu.Append(-1, "&A*", "Executa o algoritmo A*")
        self.graphMenu.AppendSeparator()
        self.exitItem = self.graphMenu.Append(wx.ID_EXIT)
        # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # menu bar
        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        self.menuBar = wx.MenuBar()
        self.menuBar.Append(self.graphMenu, "&Grafo")
        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.evt.on_insert_vertex, self.insert_vertex)
        self.Bind(wx.EVT_MENU, self.evt.on_insert_edge, self.insert_edge)
        self.Bind(wx.EVT_MENU, self.evt.on_remove_vertex, self.remove_vertex)
        self.Bind(wx.EVT_MENU, self.evt.on_remove_edge, self.remove_edge)
        self.Bind(wx.EVT_MENU, self.evt.on_check_adjacency, self.check_adjacency)
        self.Bind(wx.EVT_MENU, self.evt.on_return_edge_element, self.return_edge_element)
        self.Bind(wx.EVT_MENU, self.evt.on_return_vertex_element, self.return_vertex_element)
        self.Bind(wx.EVT_MENU, self.evt.on_return_vertices_references_from_edge, self.return_vertices_references_from_edge)
        self.Bind(wx.EVT_MENU, self.evt.on_check_planar_graph, self.check_planar_graph)
        self.Bind(wx.EVT_MENU, self.evt.on_breadth_search, self.breadth_search)
        self.Bind(wx.EVT_MENU, self.evt.on_depth_search, self.depth_search)
        self.Bind(wx.EVT_MENU, self.evt.on_prim, self.prim)
        self.Bind(wx.EVT_MENU, self.evt.on_greed_coloring, self.green_coloring)
        self.Bind(wx.EVT_MENU, self.evt.on_floyd, self.floyd)
        self.Bind(wx.EVT_MENU, self.evt.on_dijkstra, self.dijkstra)
        self.Bind(wx.EVT_MENU, self.evt.on_a_star, self.a_star)
        self.Bind(wx.EVT_MENU, self.evt.on_exit, self.exitItem)

        # desabilita as opções de menu não implementadas
        self.graphMenu.Enable(self.graphMenu.GetMenuItems()[8].GetId(), False)
        self.graphMenu.Enable(self.graphMenu.GetMenuItems()[11].GetId(), False)

        # Give the menu bar to the frame
        self.SetMenuBar(self.menuBar)

    def set_evt_handler(self, evt):
        self.evt = evt

    def show_input_dialog(self, title='Text Entry', text='Enter some text', value=""):
        dlg = wx.TextEntryDialog(self, text, title)
        dlg.SetValue(value)
        if dlg.ShowModal() == wx.ID_OK:
            # print('You entered: %s\n' % dlg.GetValue())
            return dlg.GetValue()
        dlg.Destroy()
        return None

    def draw_graph(self, file="graph.gv.png"):
        image = wx.Image(file)
        apil = self.imageToPil(image)
        width, height = apil.size
        apilr = apil.resize((int(width * self.factor), int(height * self.factor)), PIL.Image.NEAREST)
        myWxImage = wx.Image(apilr.size[0], apilr.size[1])
        myWxImage.SetData(apilr.convert('RGB').tobytes())
        self.bitmap = myWxImage.ConvertToBitmap()
        self.scrolled_panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.scrolled_panel.Refresh()
        self.scrolled_panel.Update()

    def imageToPil(self, myWxImage):
        w, h = myWxImage.GetWidth(), myWxImage.GetHeight()
        buf  = myWxImage.GetDataBuffer()
        arr  = np.frombuffer(buf, dtype='uint8')
        myPilImage = PIL.Image.frombytes("RGB", (w, h), arr.tobytes('C'))
        return myPilImage

    def on_paint(self, evt):
        dc = wx.PaintDC(self.scrolled_panel)
        dc.DrawBitmap(self.bitmap, (0, 0))

    def on_scroll(self, evt):
        ival = self.hslider.GetValue()
        self.factor = ival/100
        self.draw_graph()

    def main_loop(self):
        app.MainLoop()
