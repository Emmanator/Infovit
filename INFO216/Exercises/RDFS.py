import owlrl
from rdflib import Graph, Literal, RDF, Namespace, BNode, RDFS, XSD
from rdflib.namespace import FOAF
import requests
import urllib
from urllib import parse
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import Graph

SERVER = 'http://localhost:9999/blazegraph/'
NAMESPACE = 'ns1'

g = Graph()

endpoint = f'{SERVER}namespace/{NAMESPACE}/sparql'
client = SPARQLWrapper(endpoint)
client.setReturnFormat('json')

g = Graph()
ex = Namespace('http://example.org')

g.bind('ex', ex)
g.bind('foaf', FOAF)

# g.add((ex.Rick_Gates, RDF.type, ex.under_investigation))
# g.add((ex.under_investigation, RDFS.subClassOf, FOAF.Person))
g.add((ex.under_investigation, RDFS.domain, FOAF.Person))
g.add((ex.charged_with, RDFS.subPropertyOf, ex.under_investigation))
g.add((ex.offense, RDFS.subPropertyOf, ex.charged_with))

g.add((ex.Rick_Gates, ex.charged_with, ex.money_laundering))
g.add((ex.Rick_Gates, ex.charged_with, ex.tax_evasion))


# g.add((ex.charged_with, RDFS.subPropertyOf, ex.offense))
# g.add((ex.money_laundering, RDF.type, ex.offence))
# g.add((ex.tax_evasion, RDF.type, ex.offence))

RDF_type = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?t 

WHERE {
    ?s rdf:type ns1:Rick_Gates .
}
"""

owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(g)
print(g.serialize())
