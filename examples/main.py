import os
from grafoMaker import GrafoMaker

DEBUG = 0
if "DEBUG" in os.environ:
    DEBUG = int(os.environ["DEBUG"])

g = GrafoMaker(debug=DEBUG)

print(g.insertVertex("A"))
print(g.insertVertex("B"))
print(g.insertVertex("C"))

g.insertEdge("A", "B", "AB")
g.insertEdge("A", "C", "AC")

g.removeVertex("A")

g.renderGraph()