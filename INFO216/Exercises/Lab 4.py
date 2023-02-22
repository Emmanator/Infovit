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

president_dictionary = """
prefix ns1: <http://example.org#>

SELECT ?president ?name
WHERE {
  ?s ns1:name ?name;
  ns1:outcome ns1:indictment;
  ns1:president ?president
}
ORDER BY DESC(?president)"""

trump_pardoned = """
prefix ns1: <http://example.org#>

ASK?name (COUNT(?name) as ?count)
WHERE {
  ?s ns1:name ?name;
   ns1:pardoned ns1:true;
   ns1:president ns1:Donald_Trump
}
ASK """

test = g.query(trump_pardoned)
for row in test:
    print(row)

dict = {}
# for press, person in test:
#
#     if press not in dict:
#         dict[press] = [person]
#     else:
#         dict[press].append(person)
#     # print(press, person)
# print(dict)

#dictict = {}
#for i in test:
#    for j in i:
#        dictict[i].append(j)

#print(dictict)


