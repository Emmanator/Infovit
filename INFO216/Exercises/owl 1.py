from owlrl import OWLRL_Semantics
from rdflib import Graph, Namespace, Literal, BNode, RDF, RDFS, DC, FOAF, XSD, OWL
from rdflib.collection import Collection
import owlrl

ex = Namespace('http://example.org/')
schema = Namespace('https://schema.org/')
dbpedia = Namespace("https://dbpedia.org/page/")

g = Graph()
g.bind('ex', ex)
g.bind('foaf', FOAF)
g.bind("dbr", dbpedia)

robert = ex.Robert_Mueller
donald = ex.Donald_Trump
paul = ex.Paul_Manafort
rick = ex.Rick_Gates
cohen = ex.Michael_Cohen
flynn = ex.Michael_Flynn
investigation = ex.Mueller_Investigation

# People involved in the mueller investigation
people = [(paul, "Paul Manafort"),
          (rick, "Rick Gates"),
          (ex.George_Papadopoulos, "George Papadopoulos"),
          (flynn, "Michael Flynn"),
          (cohen, "Michael Cohen"),
          (ex.Roger_Stone, "Roger Stone")]

# a for loop to simplify adding these people to the graph
for p, name in people:
    g.add((p, RDF.type, FOAF.Person))
    g.add((p, FOAF.name, Literal(name)))
    g.add((ex.Mueller_Investigation, ex.involved, p))

# Donald Trump and Robert Mueller are two different persons.
g.add((donald, OWL.differentFrom, robert))

# Actually, all the names mentioned in connection with the Mueller investigation refer to different people.
b1 = BNode()
b2 = BNode()
Collection(g, b2, [p[0] for p in people])

g.add((b1, RDF.type, OWL.AllDifferent))
g.add((b1, OWL.distinctMembers, b2))

# All these people are foaf:Persons as well as schema:Persons)
g.add((FOAF.Person, OWL.equivalentClass, schema.Person))

# Tax evasion is a kind of bank and tax fraud.
g.add((ex.tax_evasion, RDF.type, ex.Bank_And_Tax_Fraud))
# g.add((ex.tax_evasion, ))

# The Donald Trump involved in the Mueller investigation is dbpedia:Donald_Trump and not dbpedia:Donald_Trump_Jr.
g.add((donald, OWL.sameAs, dbpedia.Donald_Trump))
g.add((donald, OWL.differentFrom, dbpedia.Donald_Trump_Jr))

# Congress, FBI and the Mueller investigation are foaf:Organizations.
g.add((ex.congress, RDF.type, FOAF.Organization))
g.add((ex.FBI, RDF.type, FOAF.Organization))
g.add((investigation, RDF.type, FOAF.Organization))

# Nothing can be both a person and an organization.
g.add((FOAF.Person, OWL.disjointWith, FOAF.Organization))

# Leading an organization is a way of being involved in an organization.
g.add((ex.leads, RDFS.subPropertyOf, ex.involved_in))

# Being a campaign manager or an advisor for is a way of supporting someone.
g.add((ex.campaign_manager_of, RDFS.subPropertyOf, ex.supports))
g.add((ex.advisor_of, RDFS.subPropertyOf, ex.supports))

# Donald Trump is a politician and a Republican.
g.add((donald, RDF.type, ex.Politician))
g.add((donald, RDF.type, ex.Republican))

# A Republican politician is both a politician and a Republican.
b3 = BNode()
Collection(g, b3, [ex.Politician, ex.Republican])
g.add((ex.Republican_Politician, OWL.intersectionOf, b3))

# Look through the predicates (properties) above and add new triples for each one that describes them as any of the
# following: a reflexive, irreflexive, symmetric, asymmetric, transitive, functional, or an inverse functional property.
g.add((ex.Paul_Manafort, ex.hasBusinessPartner, ex.Rick_Gates))
g.add((ex.Michael_Flynn, ex.adviserTo, ex.Donald_Trump))
g.add((ex.Rick_Gates_Lying, ex.wasLyingTo, ex.FBI))
g.add((ex.Donald_Trump, ex.presidentOf, ex.USA))
g.add((ex.USA, ex.hasPresident, ex.Donald_Trump))

g.add((ex.hasBusinessPartner, RDF.type, OWL.ReflexiveProperty))
g.add((ex.hasBusinessPartner, RDF.type, OWL.SymmetricProperty))
g.add((ex.hasBusinessPartner, RDF.type, OWL.TransitiveProperty))

g.add((ex.adviserTo, RDF.type, OWL.IrreflexiveProperty))

g.add((ex.wasLyingTo, RDF.type, OWL.IrreflexiveProperty))

g.add((ex.presidentOf, RDF.type, OWL.FunctionalProperty))
g.add((ex.presidentOf, RDF.type, OWL.InverseFunctionalProperty))
g.add((ex.presidentOf, RDF.type, OWL.IrreflexiveProperty))
g.add((ex.presidentOf, RDF.type, OWL.AsymmetricProperty))

g.add((ex.hasPresident, OWL.inverseOf, ex.presidentOf))

# Rules
g.add((ex.person_under_investigation, RDFS.subClassOf, FOAF.Person))
g.add((ex.charged_with, RDFS.domain, ex.Person_Under_Investigation))
g.add((ex.charged_with, RDFS.range, ex.Offense))
g.add((ex.charged_with, RDF.type, OWL.AsymmetricProperty))

g.add((ex.Rick_Gates, ex.charged_with, ex.money_laundering))
g.add((ex.Rick_Gates, ex.charged_with, ex.tax_evasion))

# Prints all triples in this assignment
owlrl.DeductiveClosure(OWLRL_Semantics).expand(g)
with open('graph.owl-xml', 'w') as f:
    f.write(g.serialize(format='xml'))
