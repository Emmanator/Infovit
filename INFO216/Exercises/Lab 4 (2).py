from SPARQLWrapper import SPARQLWrapper

SERVER = 'http://localhost:9999/blazegraph/'
NAMESPACE = 'ns1'

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
    ?s ?p ?o
}
"""
# s = set()
# for row in results["results"]["bindings"]:
#     for r in row:
#         s.add(row[r]["type"])
#     # print(row)
# print(s)


client.setQuery(types)
# print('Spouses:')
results = client.queryAndConvert()
s = set()
for row in results["results"]["bindings"]:
    for r in row:
        s.add(row[r]["type"])
    # print(row)
print(s)

# FILTER  (?start < "1990-01-01")
# FILTER  (?end > "2090-01-01")
# ["name"]["value"]
# BIND(REPLACE(REPLACE(REPLACE(STR(?o), STR(ns1:), ''), '_', ' '), '%2C', ',') AS ?test)
