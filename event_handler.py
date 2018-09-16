from graph_maker import GraphMaker

class EventHandler:
    def __init__(self, gui, debug=None):
        self.gui = gui
        self.debug = debug
        self.graph = GraphMaker(self.debug)

    def on_insert_vertex(self, evt):
        if self.debug == 2:
            vertex = "A"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "B"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "C"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Inserir vértice", text="Informe o Vértice: ")
            if value is not None:
                vertex = value
                ret = self.graph.insert_vertex(vertex)
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_insert_edge(self, evt):
        if self.debug == 2:
            ret = self.graph.insert_edge("A", "B", str('AB'))
            self.print_feedback(ret)
            ret = self.graph.insert_edge("B", "A")
            self.print_feedback(ret)
            ret = self.graph.insert_edge("A", "C", str('AC'))
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            values = []
            v = self.gui.show_input_dialog(title="Inserir aresta", text="Informe o 1o vértice: ")
            if v is not None:
                values.append(v)
            v = self.gui.show_input_dialog(title="Inserir aresta", text="Informe o 2o vértice: ")
            if v is not None:
                values.append(v)
            v = self.gui.show_input_dialog(title="Inserir aresta", text="Informe a aresta: ")
            if v is not None:
                values.append(v)
            if len(values) > 2:
                ret = self.graph.insert_edge(values[0], values[1], str(values[2]))
            else:
                ret = self.graph.insert_edge(values[0], values[1])
            self.on_draw_graph(evt)
            self.print_feedback(ret)

    def on_remove_vertex(self, evt):
        if self.debug == 2:
            ret = self.graph.remove_vertex(0)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Remover vértice", text="Informe a referência do vértice")
            if value is not None:
                ret = self.graph.remove_vertex(int(value))
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_remove_edge(self, evt):
        if self.debug == 2:
            ret = self.graph.remove_edge(0)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Remover aresta", text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.remove_edge(int(value))
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_check_adjacency(self, evt):
        if self.debug == 2:
            ret = self.graph.check_adjacency("A", "C")
            self.print_feedback(ret)
            ret = self.graph.check_adjacency("A", "B")
            self.print_feedback(ret)
        else:
            values = []
            v = self.gui.show_input_dialog(title="Verificar adjacência", text="Informe o 1o vértice: ")
            if v is not None:
                values.append(v)
            v = self.gui.show_input_dialog(title="Verificar adjacência", text="Informe o 2o vértice: ")
            if v is not None:
                values.append(v)
            ret = self.graph.check_adjacency(values[0], values[1])
            self.print_feedback(ret)

    def on_return_edge_element(self, evt):
        if self.debug == 2:
            ret = self.graph.return_edge_element(0)
            self.print_feedback(ret)
            ret = self.graph.return_edge_element(1)
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar elemento da aresta", text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.return_edge_element(int(value))
                self.print_feedback(ret)

    def on_return_vertex_element(self, evt):
        if self.debug == 2:
            ret = self.graph.return_vertex_element(0)
            self.print_feedback(ret)
            ret = self.graph.return_vertex_element(1)
            self.print_feedback(ret)
            ret = self.graph.return_vertex_element(3)
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar elemento do vértice", text="Informe a referência do vértice")
            if value is not None:
                ret = self.graph.return_vertex_element(int(value))
                self.print_feedback(ret)

    def on_return_vertices_references_from_edge(self, evt):
        if self.debug == 2:
            ret = self.graph.return_vertices_references_from_edge(0)
            self.print_feedback(ret)
            ret = self.graph.return_vertices_references_from_edge(1)
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar referência dos vértices da aresta", text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.return_vertices_references_from_edge(int(value))
                self.print_feedback(ret)

    def on_check_planar_graph(self, evt):
        ret = self.graph.check_planar_graph()
        self.print_feedback(ret)

    def on_breadth_search(self, evt):
        ret = self.graph.breadth_search()
        self.print_feedback(ret)

    def on_depth_search(self, evt):
        ret = self.graph.depth_search()
        self.print_feedback(ret)

    def on_prim(self, evt):
        ret = self.graph.prim()
        self.print_feedback(ret)

    def on_draw_graph(self, evt):
        self.graph.draw_graph()
        self.gui.draw_graph()

    def print_feedback(self, message):
       self.gui.text_area.AppendText(message + "\n")
