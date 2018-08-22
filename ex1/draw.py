from graphviz import Digraph

g = Digraph('G', filename='hello.gv',)

g.edge('Hello', 'World')
g.edge('a', 'b')
g.edge('b','c')
g.edge('c','a')
g.edge('a','d')
g.edge('d','e')

# g.view()
g.render(filename='hello.gv', view=False)