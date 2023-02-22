from rdflib import Graph

g = Graph()

g.parse('C:/Infovit/INFO216/Russia_investigation_kg.ttl', format('ttl'))

all_predicates_query = """
prefix ns1: <http://example.org#>
SELECT ?p
WHERE
{
  ?s ?p ?o
}
"""

sorted_presidents = """
prefix ns1: <http://example.org#>

SELECT DISTINCT ?o

WHERE {
    ?s ns1:president ?o
}
ORDER BY ASC(UCASE(str(?o)))
"""




test = g.query(sorted_presidents)
for row in test:
    print(f'Predicates: {row}')
