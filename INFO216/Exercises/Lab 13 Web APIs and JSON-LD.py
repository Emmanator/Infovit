import requests
from rdflib import FOAF, Namespace, Literal, RDF, Graph

r = requests.get('http://api.open-notify.org/astros.json').json()

g = Graph()
ex = Namespace('http://example.org/')

g.bind("ex", ex)
NS = {
    "ex": ex,
    "foaf":FOAF
}

#Write a small program that queries the Open Notify Astros API
for item in r['people']:
    craft = item['craft'].replace(" ","_")
    person = item['name'].replace(" ","_")
    g.add((ex[person], ex.onCraft, ex[craft]))
    g.add((ex[person], RDF.type, FOAF.Person))
    g.add((ex[person], FOAF.name, Literal(item['name'])))
    g.add((ex[craft], FOAF.name, Literal(item['craft'])))

res = g.query("""
    CONSTRUCT {?person1 foaf:knows ?person2}
    WHERE {
        ?person1 ex:onCraft ?craft .
        ?person2 ex:onCraft ?craft .
        }
""", initNs=NS)

for triplet in res:
    # (we don't need to add that they know themselves)
    if (triplet[0] != triplet[2]):
        g.add((triplet))

#Serialise the graph to JSON-LD
print(g.serialize(format="json-ld"))

#DBpedia Spotlight was worked on Lab 5 (CSV to RDF).