import os
from grafoMaker import GrafoMaker

DEBUG = 0
if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

g = GrafoMaker(debug=DEBUG)

print(g.insertVertex("A"))
print(g.insertVertex("B"))
print(g.insertVertex("C"))

print(g.insertEdge("A", "B", "AB"))
print(g.insertEdge("A", "C", "AC"))

g.removeVertex("A")
# g.removeEdge() #TODO

# g.checkAdjacency() #TODO

# g.returnEdgeElement() #TODO
# g.returnVertexElement() #TODO
# g.return2VertexReferences() #TODO

g.render_graph()
