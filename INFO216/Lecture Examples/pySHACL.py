from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
data_graph.parse('...')

shacl_str = """a"""
shacl_graph = Graph()
shacl_graph.parse(
    data=shacl_str, format='ttl'
)

results = validate(
    data_graph,
    shacl_graph=shacl_graph,
    inference='both'
)
(conforms,
 results_graph,
 results_text) = results
print(results_text)
