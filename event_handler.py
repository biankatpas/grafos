from graph_maker import GraphMaker

class EventHandler:
    def __init__(self, gui, debug=None):
        self.gui = gui
        self.graph = GraphMaker(debug)

    # TODO: pedir todos os dados para o usuario

    def OnInsertVertex(self, evt):
        vertex = "A"
        ret = self.graph.insertVertex(vertex)
        self.print_feedback(ret)

        vertex = "B"
        ret = self.graph.insertVertex(vertex)
        self.print_feedback(ret)

        vertex = "C"
        ret = self.graph.insertVertex(vertex)
        self.print_feedback(ret)

    def OnInsertEdge(self, evt):
        ret = self.graph.insertEdge("A", "B", str('AB'))
        self.print_feedback(ret)

    def OnRemoveVertex(self, evt):
        ret = self.graph.removeVertex(2)
        self.print_feedback(ret)

    def OnRemoveEdge(self, evt):
        ret = self.graph.removeEdge(0)
        self.print_feedback(ret)

    def OnCheck2VertexAdjacency(self, evt):
        ret = self.graph.checkAdjacency("A", "C")
        self.print_feedback(ret)
        ret = self.graph.checkAdjacency("A", "B")
        self.print_feedback(ret)

    def OnReturnEdgeElement(self, evt):
        ret = self.graph.returnEdgeElement(0)
        self.print_feedback(ret)
        ret = self.graph.returnEdgeElement(1)
        self.print_feedback(ret)

    def OnReturnVertexElement(self, evt):
        ret = self.graph.returnVertexElement(0)
        self.print_feedback(ret)
        ret = self.graph.returnVertexElement(1)
        self.print_feedback(ret)
        ret = self.graph.returnVertexElement(3)
        self.print_feedback(ret)

    def OnReturnEdge2VertexReferences(self, evt):
        ret = self.graph.return2EdgeVertexReferences(0)
        self.print_feedback(ret)
        ret = self.graph.return2EdgeVertexReferences(1)
        self.print_feedback(ret)

    def print_feedback(self, message):
       self.gui.text_area.AppendText(message + "\n")

    # todo: vitor
    def OnCheckPlanarGraph(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def OnBreadthSearch(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def OnDepthSearch(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def OnPRIM(self, evt):
        ret = "vitor"
        self.print_feedback(ret)
