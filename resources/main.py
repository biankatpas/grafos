import os
from grafoMaker import GrafoMaker

DEBUG = 0
if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

g = GrafoMaker(debug=DEBUG)

print(g.insert_vertex("A"))
print(g.insert_vertex("B"))
print(g.insert_vertex("C"))

print(g.insert_edge("A", "B", "AB"))
print(g.insert_edge("A", "C", "AC"))

g.remove_vertex("A")
# g.removeEdge() #TODO

# g.checkAdjacency() #TODO

# g.returnEdgeElement() #TODO
# g.returnVertexElement() #TODO
# g.return2VertexReferences() #TODO

g.draw_graph()
