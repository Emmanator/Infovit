from rdflib import Graph, Namespace, Literal, BNode, RDF, RDFS, DC, FOAF, XSD

EX = Namespace('http://example.org/')

g = Graph()
g.bind('ex', EX)  # this is why the line '@prefix ex: <http://example.org/> .'
                  # and the 'ex.' prefix are used when we print out Turtle later
