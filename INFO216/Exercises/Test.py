from rdflib import Graph
from rdflib import URIRef

g = Graph()

g.parse("http://www.w3.org/People/Berners-Lee/card")

# Loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    # Check if there is at least one triple in the Graph
    if (subj, pred, obj) not in g:
        raise Exception("haha")

print(f"Graph g has {len(g)} statements")

print(g.serialize(format="turtle"))

donaldTrump = URIRef('http://example.org/Donald_Trump')
