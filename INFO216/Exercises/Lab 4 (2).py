from SPARQLWrapper import SPARQLWrapper, JSON, XML
from rdflib import Graph

SERVER = 'http://localhost:9999/blazegraph/'
NAMESPACE = 'ns1'

g = Graph()

endpoint = f'{SERVER}namespace/{NAMESPACE}/sparql'
client = SPARQLWrapper(endpoint)
client.setReturnFormat('json')

query1990 = """
prefix ns1: <http://example.org#>

ASK {
SELECT ?s
WHERE
    {
  ?s ns1:investigation_start ?start ;
    ns1:investigation_end ?end
    
    BIND(REPLACE(STR(?end), STR(ns1:), '') AS ?end_date)
    FILTER  (?end_date >= "1990-01-01")
    
    BIND(REPLACE(STR(?start), STR(ns1:), '') AS ?start_date)
    FILTER  (?start_date <= "1990-01-01")
    }
}
"""

describ100 = """
prefix ns1: <http://example.org#>

DESCRIBE ns1:investigation_100
"""

types = """
prefix ns1: <http://example.org#>

SELECT *
WHERE{
    ?s ns1:person ?o
}
"""
# s = set()
# for row in results["results"]["bindings"]:
#     for r in row:
#         s.add(row[r]["type"])
#     # print(row)
# print(s)


gwaph_update = """
prefix ns1: <http://example.org#>

INSERT {?o rdf:type ns1:IndictedPerson}

WHERE {
    ?s ns1:person ?o
} """


title_update = """
prefix ns1: <http://example.org#>

INSERT {?o dc:title ?test}

WHERE {
    ?s ns1:investigation ?o
    BIND(REPLACE(REPLACE(REPLACE(STR(?o), STR(ns1:), ''), '_', ' '), '%2C', ',') AS ?test)
}

"""

indicted_sorted = """
prefix ns1: <http://example.org#>

SELECT *

WHERE {
    ?s rdf:type ns1:IndictedPerson
}
ORDER BY ?s
"""


indicted_days = """
prefix ns1: <http://example.org#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT (MAX(?t) AS ?max) (MIN(?t) AS ?min) (AVG(xsd:double(?t)) AS ?avg) ?i

WHERE {
    ?s ns1:indictment_days ?o ;
        ns1:investigation ?i
    BIND(REPLACE(STR(?o), STR(ns1:), '')AS ?t)
    FILTER(?t != 'nan')
}
GROUP BY ?i
"""


describe_stone = """
prefix ns1: <http://example.org#>

DESCRIBE ns1:Oliver_North
"""

client.setQuery(describe_stone)
# client.method = 'POST'
# client.query()
client.setReturnFormat(XML)


# print('Spouses:')
results = client.queryAndConvert()
s = list()

#for row in results["results"]["bindings"]:
#    for r in row:
#        print(row[r]['value'])
        # if row[r]['value'] != 'nan':
        #     s.append(float(row[r]['value']))

    # print(row)
# print(sum(s)/len(s))

# FILTER  (?start < "1990-01-01")
# FILTER  (?end > "2090-01-01")
# ["name"]["value"]
# BIND(REPLACE(REPLACE(REPLACE(STR(?o), STR(ns1:), ''), '_', ' '), '%2C', ',') AS ?test)

print(type(results))
print(results.serialize(format='ttl'))
