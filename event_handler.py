from graph_maker import GraphMaker

class EventHandler:
    def __init__(self, gui, debug=None):
        self.gui = gui
        self.graph = GraphMaker(debug)

    def OnInsertVertex(self, evt):
        vertex = "A"
        ret = self.graph.insertVertex(vertex)
        self.print_feedback("Inserido vértice: " + vertex + ". Referência", ret)
        self.gui.renderGraph()

        vertex = "B"
        ret = self.graph.insertVertex(vertex)
        self.print_feedback("Inserido vértice: " + vertex + ". Referência", ret)
        self.gui.renderGraph()

    def OnInsertEdge(self, evt):
        ret = self.graph.insertEdge("A", "B", str('AB'))
        self.print_feedback("Inserida aresta", ret)
        self.gui.renderGraph()

    def OnRemoveVertex(self, evt):
        print('todo')

    def OnRemoveEdge(self, evt):
        print('todo')

    def OnCheck2VertexAdjacency(self, evt):
        print('todo')

    def OnReturnEdgeElement(self, evt):
        print('todo')

    def OnReturnVertexElement(self, evt):
        print('todo')

    def OnReturn2VertexReferences(self, evt):
        print('todo')

    def OnCheckPlanarGraph(self, evt):
        print('todo')

    def OnBreadthSearch(self, evt):
        print('todo')

    def OnDepthSearch(self, evt):
        print('todo')

    def OnPRIM(self, evt):
        print('todo')

    def print_feedback(self, evt, ret):
        if ret is not None:
            self.gui.text_area.Clear()
            self.gui.text_area.AppendText(evt + " :" + str(ret) + "\n")
        else:
            self.gui.text_area.Clear()
            self.gui.text_area.AppendText("Já existe no grafo, não inserido.")