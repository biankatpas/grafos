from graphviz import Digraph

g = Digraph('G', filename='graph.gv')

g.edge('Hello', 'World', label='a')
g.edge('a', 'b')
g.edge('a', 'c')
g.edge('a','d')
g.edge('a','e')
g.edge('b','c')
g.edge('b','d')
g.edge('d','e')

# g.view()
g.render(filename='graph.gv', view=False)