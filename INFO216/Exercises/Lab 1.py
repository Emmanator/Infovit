from rdflib import Graph, Literal, RDF, Namespace
from rdflib.namespace import FOAF
import requests
import urllib
from urllib import parse

g = Graph()

# variables to easily find these again, without having to type it so often.
custom = Namespace("http://example.org/")
robert = custom.Robert_Mueller
donald = custom.Donald_Trump
paul = custom.Paul_Manafort
rick = custom.Rick_Gates
cohen = custom.Michael_Cohen
flynn = custom.Michael_Flynn
investigation = custom.Mueller_Investigation

g.add((robert, RDF.type, FOAF.Person))
g.add((robert, FOAF.name, Literal("Robert Mueller")))
g.add((robert, custom.leads, custom.Mueller_Investigation))

g.add((donald, RDF.type, FOAF.Person))
g.add((donald, FOAF.name, Literal("Donald Trump")))

# People involved in the mueller investigation
people = [(paul, "Paul Manafort"),
          (rick, "Rick Gates"),
          (custom.George_Papadopoulos, "George Papadopoulos"),
          (flynn, "Michael Flynn"),
          (cohen, "Michael Cohen"),
          (custom.Roger_Stone, "Roger Stone")]

# a for loop to simplify adding these people to the graph
for p, name in people:
    g.add((p, RDF.type, FOAF.Person))
    g.add((p, FOAF.name, Literal(name)))
    g.add((custom.Mueller_Investigation, custom.involved, p))

# Paul Manafort Things
g.add((paul, custom.business_partner, custom.Rick_Gates))
g.add((paul, custom.employer, donald))
g.add((paul, custom.job, custom.campaign_manager))
g.add((paul, custom.charged, custom.tax_evasion))
g.add((paul, custom.charged, custom.money_laundering))
g.add((paul, custom.charged, custom.foreign_lobbying))
g.add((paul, custom.convicted, custom.bank_fraud))
g.add((paul, custom.convicted, custom.tax_fraud))
g.add((paul, custom.plead_guilty, custom.conspiracy))
g.add((paul, custom.sentenced, custom.prison))
g.add((paul, custom.negotiate, custom.plea_agreement))

# Rick Stone things
g.add((rick, custom.charged, custom.tax_evasion))
g.add((rick, custom.charged, custom.money_laundering))
g.add((rick, custom.charged, custom.foreign_lobbying))
g.add((rick, custom.plead_guilty, custom.conspiracy))
g.add((rick, custom.plead_guilty, custom.lying_to_fbi))

# Michael Cohen things
g.add((cohen, custom.attorney, donald))
g.add((cohen, custom.plead_guilty, custom.lying_to_congress))

# Michael Flynn Things
g.add((flynn, custom.adviser, donald))
g.add((flynn, custom.plead_guilty, custom.lying_to_fbi))
g.add((flynn, custom.negotiate, custom.plea_deal))

# For ever triple in G, if G == plead_guilty, print triple
for subj, pred, obj in g:
    if pred == custom.plead_guilty:
        print(subj, pred, obj)

# Personally I found XML to be the cleanest for this, but the other options work too.
print(g.serialize(format='ttl'))


# Method that gets information from rdf-grapher and saves it to file
def get_image(graph):
    g = urllib.parse.quote_plus(graph.serialize(format='ttl'))
    response = requests.get(f'http://www.ldf.fi/service/rdf-grapher?rdf={g}&from=ttl&to=png')
    response.raise_for_status()
    with open("response.png", "wb") as f:
        f.write(response.content)


get_image(g)
