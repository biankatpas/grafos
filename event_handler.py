from graph_maker import GraphMaker

class EventHandler:
    def __init__(self, gui, debug=None):
        self.gui = gui
        self.graph = GraphMaker(debug)

    # TODO: pedir todos os dados para o usuario

    def on_insert_vertex(self, evt):
        vertex = "A"
        ret = self.graph.insert_vertex(vertex)
        self.print_feedback(ret)

        vertex = "B"
        ret = self.graph.insert_vertex(vertex)
        self.print_feedback(ret)

        vertex = "C"
        ret = self.graph.insert_vertex(vertex)
        self.print_feedback(ret)

    def on_insert_edge(self, evt):
        ret = self.graph.insert_edge("A", "B", str('AB'))
        self.print_feedback(ret)

    def on_remove_vertex(self, evt):
        ret = self.graph.remove_vertex(2)
        self.print_feedback(ret)

    def on_remove_edge(self, evt):
        ret = self.graph.remove_edge(0)
        self.print_feedback(ret)

    def on_check_2_vertex_adjacency(self, evt):
        ret = self.graph.check_adjacency("A", "C")
        self.print_feedback(ret)
        ret = self.graph.check_adjacency("A", "B")
        self.print_feedback(ret)

    def on_return_edge_element(self, evt):
        ret = self.graph.return_edge_element(0)
        self.print_feedback(ret)
        ret = self.graph.return_edge_element(1)
        self.print_feedback(ret)

    def on_return_vertex_element(self, evt):
        ret = self.graph.return_vertex_element(0)
        self.print_feedback(ret)
        ret = self.graph.return_vertex_element(1)
        self.print_feedback(ret)
        ret = self.graph.return_vertex_element(3)
        self.print_feedback(ret)

    def on_return_edge_2_vertex_references(self, evt):
        ret = self.graph.return_2_edge_vertex_references(0)
        self.print_feedback(ret)
        ret = self.graph.return_2_edge_vertex_references(1)
        self.print_feedback(ret)

    def print_feedback(self, message):
       self.gui.text_area.AppendText(message + "\n")

    # todo: vitor
    def on_check_planar_graph(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def on_breadth_search(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def on_depth_search(self, evt):
        ret = "vitor"
        self.print_feedback(ret)

    def on_prim(self, evt):
        ret = "vitor"
        self.print_feedback(ret)
