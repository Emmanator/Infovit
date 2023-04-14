import owlrl
from rdflib import Graph, Literal, RDF, Namespace, BNode, RDFS, XSD, OWL
from rdflib.namespace import FOAF
import requests
import urllib
from urllib import parse


g = Graph()
ex = Namespace('http://example.org')

g.bind('ex', ex)
g.bind('foaf', FOAF)

# g.add((ex.Cade, RDF.type, ex.Student))
# g.add((ex.Cade, ex.studentat, ex.UIB))

# g.add((ex.Person, RDFS.subClassOf, ex.Investigation))
g.add((ex.charged_with, RDFS.subPropertyOf, ex.under_investigation))
g.add((ex.Money_laundering, RDFS.subPropertyOf, ex.offense))
g.add((ex.Tax_Evasion, RDFS.subPropertyOf, ex.offense))

g.add((ex.Person, ex.under_investigation, FOAF.Person))

g.add((ex.Rick_Gates, RDF.type, ex.Person))
g.add((ex.Rick_Gates, ex.charged_with, ex.Money_laundering))
g.add((ex.Rick_Gates, ex.charged_with, ex.Tax_Evasion))

g.add((ex.Paul_Manafort, RDF.type, ex.Person))
g.add((ex.Paul_Manafort, ex.convicted, ex.Tax_Evasion))


owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(g)
print(g.serialize())
