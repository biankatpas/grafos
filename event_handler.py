from graph_maker import GraphMaker


class EventHandler:
    def __init__(self, gui, debug=None):
        self.gui = gui
        self.debug = debug
        self.directed = True
        self.graph = GraphMaker(self, self.directed, self.debug)

    def on_insert_vertex(self, evt):
        if self.debug >= 50:
            vertex = "S"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "X"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "U"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "Y"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            vertex = "V"
            ret = self.graph.insert_vertex(vertex)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Inserir vértice", text="Informe o Vértice: ")
            if value is not None:
                ret = self.graph.insert_vertex(value)
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_insert_edge(self, evt):
        if self.debug >= 50:
            ret = self.graph.insert_edge("S", "U", 10)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("S", "X", 5)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("X", "U", 3)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("X", "V", 9)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("X", "Y", 2)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("U", "X", 2)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("U", "V", 1)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("Y", "S", 7)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("Y", "V", 6)
            self.print_feedback(ret)
            ret = self.graph.insert_edge("V", "Y", 4)
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
            v = self.gui.show_input_dialog(title="Inserir aresta", text="Informe o peso: ")
            if v is not None:
                    values.append(v)
            v = self.gui.show_input_dialog(title="Inserir aresta", text="Informe a aresta: ")
            if v is not None:
                values.append(v)
            if len(values) > 3:
                ret = self.graph.insert_edge(values[0], values[1], values[2], str(values[3]))
            else:
                ret = self.graph.insert_edge(values[0], values[1], values[2])
            self.on_draw_graph(evt)
            self.print_feedback(ret)

    def on_remove_vertex(self, evt):
        if self.debug >= 50:
            ret = self.graph.remove_vertex(0)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Remover vértice", text="Informe a referência do vértice")
            if value is not None:
                ret = self.graph.remove_vertex(value)
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_remove_edge(self, evt):
        if self.debug >= 50:
            ret = self.graph.remove_edge(0)
            self.print_feedback(ret)
            self.on_draw_graph(evt)
        else:
            value = self.gui.show_input_dialog(title="Remover aresta", text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.remove_edge(value)
                self.print_feedback(ret)
                self.on_draw_graph(evt)

    def on_check_adjacency(self, evt):
        if self.debug >= 50:
            ret = self.graph.check_adjacency("S", "U")
            self.print_feedback(ret)
            ret = self.graph.check_adjacency("U", "Y")
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
        if self.debug >= 50:
            ret = self.graph.return_edge_element('AB')
            self.print_feedback(ret)
            ret = self.graph.return_edge_element('AE')
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar elemento da aresta",
                                               text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.return_edge_element(value)
                self.print_feedback(ret)

    def on_return_vertex_element(self, evt):
        if self.debug >= 50:
            ret = self.graph.return_vertex_element('A')
            self.print_feedback(ret)
            ret = self.graph.return_vertex_element('B')
            self.print_feedback(ret)
            ret = self.graph.return_vertex_element('E')
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar elemento do vértice",
                                               text="Informe a referência do vértice")
            if value is not None:
                ret = self.graph.return_vertex_element(value)
                self.print_feedback(ret)

    def on_return_vertices_references_from_edge(self, evt):
        if self.debug >= 50:
            ret = self.graph.return_vertices_references_from_edge('AB')
            self.print_feedback(ret)
            ret = self.graph.return_vertices_references_from_edge('AE')
            self.print_feedback(ret)
        else:
            value = self.gui.show_input_dialog(title="Retornar referência dos vértices da aresta",
                                               text="Informe a referência da aresta")
            if value is not None:
                ret = self.graph.return_vertices_references_from_edge(value)
                self.print_feedback(ret)

    def on_check_planar_graph(self, evt):
        ret = self.graph.check_planar_graph()
        self.print_feedback(ret)

    def on_breadth_search(self, evt):
        value = self.gui.show_input_dialog(title="Vértice inicial", text="Informe o vértice inicial")
        ret = self.graph.breadth_search(value, evt)
        self.print_feedback(ret)
        self.on_draw_graph(evt)

    def on_depth_search(self, evt):
        value = self.gui.show_input_dialog(title="Vértice inicial", text="Informe o vértice inicial")
        ret = self.graph.call_depth_search(value, evt)
        self.print_feedback(ret)
        self.on_draw_graph(evt)

    def on_prim(self, evt):
        value = self.gui.show_input_dialog(title="Vértice inicial", text="Informe o vértice inicial")
        ret = self.graph.prim(value)
        self.print_feedback(ret)

    def on_greed_coloring(self, evt):
        ret = self.graph.greed_coloring(evt)
        self.print_feedback(ret)
        self.on_draw_graph(evt)

    def on_floyd(self, evt):
        ret = self.graph.floyd()
        self.print_feedback(ret)
        self.on_draw_graph(evt)

    def on_dijkstra(self, evt):
        value = self.gui.show_input_dialog(title="Vértice inicial", text="Informe o vértice inicial")
        ret = self.graph.dijkstra(value, evt)
        self.print_feedback(ret)
        self.on_draw_graph(evt)

    def on_exit(self, event):
        self.gui.Close(True)

    def on_draw_graph(self, evt):
        self.graph.draw_graph()
        self.gui.draw_graph()

    def print_feedback(self, message):
        self.gui.text_area.AppendText(message + "\n")
