# Standard imports at the start of an rdf graph in rdflib
from rdflib import RDF, RDFS, FOAF, OWL, Namespace, Graph, XSD, Literal

# to make a graph
g = Graph()

# Graph needs a namespace
ex = Namespace('http://ex.org#')

# Assigns an OWL class to Agent a Publication
g.add((ex.Agent, RDF.type, OWL.Class))
g.add((ex.Publication, RDF.type, OWL.Class))

# Makes these classes subclasses of agent or publication
g.add((ex.Author, RDFS.subClassOf, ex.Agent))
g.add((ex.Organization, RDFS.subClassOf, ex.Agent))
g.add((ex.Country, RDFS.subClassOf, ex.Agent))
g.add((ex.Paper, RDFS.subClassOf, ex.Publication))

# This section assigns properties into the graph
# Every property needs a domain, and range.
g.add((ex.name, RDFS.domain, ex.Agent))
g.add((ex.name, RDFS.range, XSD.string))

g.add((ex.affiliation, RDFS.domain, ex.Author))
g.add((ex.affiliation, RDFS.range, ex.Organization))

g.add((ex.country, RDFS.domain, ex.Author))
g.add((ex.country, RDFS.range, ex.Country))

g.add((ex.title, RDFS.domain, ex.Publication))
g.add((ex.title, RDFS.range, XSD.string))

g.add((ex.author, RDFS.domain, ex.Publication))
g.add((ex.author, RDFS.range, ex.Author))

g.add((ex.publication, RDFS.domain, ex.Paper))
g.add((ex.publication, RDFS.range, ex.Publication))

g.add((ex.publisher, RDFS.domain, ex.Paper))
g.add((ex.publisher, RDFS.range, ex.Organization))

g.add((ex.year, RDFS.domain, ex.Publication))
g.add((ex.year, RDFS.range, XSD.int))

# This is how you'd add a paper into this graph
g.add((ex.the_semantic_web, RDF.type, ex.Paper))
g.add((ex.the_semantic_web, ex.title, Literal("The Semantic Web")))
g.add((ex.the_semantic_web, ex.author, ex.Tim_Berners_Lee))
g.add((ex.the_semantic_web, ex.author, ex.James_Hendler))
g.add((ex.the_semantic_web, ex.publication, ex.Scientific_American))
g.add((ex.the_semantic_web, ex.publisher, ex.Springer_Nature))
g.add((ex.the_semantic_web, ex.year, Literal(2001)))

# This is how you'd add an author into the graph
g.add((ex.Tim_Berners_Lee, RDF.type, ex.Author))
g.add((ex.Tim_Berners_Lee, ex.name, Literal("Tim Berners Lee")))
g.add((ex.Tim_Berners_Lee, ex.affiliation, ex.MIT))
g.add((ex.Tim_Berners_Lee, ex.country, ex.United_States))

# Restrictions
# Organization is a kind of Agent
# :Organization rdfs:subClassOf :Agent

# The object in an affiliation-triple is an Organization.
# :affiliation rdfs:range :Organization
# :affiliation rdfs:domain :Author

# A paper can only be published in 1 Publication
# :publication owl:cardinality 1

# A Paper can only have one year
# :publication rdf:type owl:FunctionalProperty
# :year owl:maxCardinality 1

# Paper cannot not be its own publication
# :publication rdf:type owl:IrreflexiveProperty
# :publication rdf:type owl:TransitiveProperty

# Two authors cannot have the same name
# :name rdf:type owl:InverseFunctionalProperty

# Author is not an Organization
# :Author owl:disjointWith :Organization

# title is a string
# :title rdfs:range xsd:string


# Paper becomes a subclass of an owl:Restriction, that says minCardinality has to be 1 for author.
# :Paper rdfs:subClassOf [ rdf:type owl:Restriction ;
#                          owl:minCardinality "1" ;
#                          owl:onProperty :author
#                        ] .
# owl:restriction on :Paper that says there has to be 1 title
# :Paper rdfs:subClassOf [ rdf:type owl:Restriction ;
#                          owl:cardinality "1" ;
#                          owl:onProperty :title
#                        ] .
# owl:DataRange restriction that says a year has to be between 1900 and 2050
# :year rdfs:range [ rdf:type owl:DataRange ;
#                    owl:minInclusive "1900" ;
#                    owl:maxInclusive "2050"
#                  ] .

# A disjointwith B, A disjoinwith C, B disjoint with C
# :Author owl:disjointWith :Organization
# :Author owl:disjointWith :Country
# :Organization owl:disjointWith :Country

# Says Publisher has to be one of these publishers.
# :Publisher owl:oneOf (:CM :IEEE_CS :Springer_Nature :IGI_Global)

# Selects titles of a paper
# SELECT ?title
# WHERE {
# ?paper rdf:type :Paper ;
#   :title ?title .
# }

# Selects distinct names of Organizations
# SELECT DISTINCT ?name
# WHERE {
#   ?p rdf:type :Publication ;
#       :publisher / :name ?name
# }
# ORDER BY ?name

# Selects name of author and title of Papers they have written
# SELECT ?name ?title
# WHERE {
#   ?author ^:name / ^:author / :title ?title
#
#   ?p :author ?a .
#   ?p rdf:type :Paper .
#   ?p :title ?title .
#   ?a :name ?name
# }

# Returns how many publications from each country
# SELECT ?c (COUNT(?p) AS ?number)
# WHERE {
# ?p rdf:type :Paper ;
#   :author / :country / :name ?c
# }
# GROUP BY ?c

# Lists authors and the number of publications
# SELECT ?a (COUNT(?p) AS ?number)
# WHERE {
# ?p rdf:type :Paper ;
#   :author / :name ?a
# }
# GROUP BY ?a
# ORDER BY ?number DESC

# Lists authors and the year of their first and last published work
# SELECT ?a (MIN(?y) as ?min) (MAX(?y) as ?max)
# WHERE {
#   ?p rdf:type :Paper ;
#       :year ?y ;
#       :author / :name ?a
# }
# GROUP BY ?a

# Return the name of Authors, excluding ones that have affiliation Germany
# SELECT ?name
# WHERE {
#   ?a rdf:type :Author ;
#       :name ?name
#   MINUS {
#       ?a :affiliation / :country / :name "Germany"
#   }
# }

# This asks if James Hendler is an author of more than 1 paper by getting p1 and p2 and comparing
# ASK {
#   ?a rdf:type :Author ;
#       :name "James Hendler" .
#   ?p1 :author ?a .
#   ?p2 :author ?a .
#   FILTER (?p1 != ?p2)
# }

# Makes a new construction in the graph of all authors have that worked with Christian_Bizer
# CONSTRUCT{
#   ?a rdf:type :Author ;
#       :affiliation ?affili ;
#       :country ?country ;
#       :name ?name
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?affili ;
#       :country ?country ;
#       :name ?name .
#   ?p rdf:type :Paper ;
#       :author :Christian_Bizer ;
#       :author ?a
# }

# Creates a new part of the graph same as above but including THEIR Papers, affiliations, and countries Related to Christian Bizer
# CONSTRUCT {
#   ?a rdf:type :Author ;
#       :affiliation ?affili ;
#       :country ?country ;
#       :name ?name .
#   ?p2 rdf:type :Paper ;
#       :author ?a2 ;
#       :title ?t .
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?affili ;
#       :country ?country ;
#       :name ?name .
#   ?p2 rdf:type :Paper ;
#       :author ?a2 ;
#       :author ?a ;
#       :title ?t .
#   ?p rdf:type :Paper ;
#       :author :Christian_Bizer ;
#       :author ?a
# }

# Says that orgs that have an affiliation with Author are a type of institution
# INSERT {
#   ?org rdf:type :Institution
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?org
# }

# If an Author has a country, then that Organization is located in that same country
# INSERT {
#   ?org :locatedIn ?country
# } WHERE {
#   ?a rdf:type :Author ;
#       :country ?country ;
#       :affiliation ?org
# }

# Paper is producedBy the Organization the author is affiliated with
# INSERT {
#   ?p :producedBy ?org
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?org ;
#       ^:author ?p
# }

# This says a paper is produced in the country that the author is locatedin
# INSERT {
#   ?p :producedIn ?c
# } WHERE {
#   ?p rdf:type :Paper ;
#       :author / :affiliation / :locatedIn ?c
# }

# This just deletes all country connections between authors and countries
# DELETE {
#   ?a :country ?c
# } WHERE {
#   ?a :country ?c
# }

# This says to delete the most recent year of a Paper if it has multiple
# DELETE {
#   ?p :year ?y2
# } WHERE {
#   ?p rdf:type :Paper ;
#       :year ?y1 ;
#       :year ?y2 
#   FILTER(?y1 < ?y2)
# }


# SHACL stuff, nightmarenightmarenightmare
# SHACL seems similar to RDFLIB tbh, you give it a nodeshape, then a targetClass, then a property.
#:LabTasks_Shape
#    a sh:NodeShape ;
#    sh:targetClass ex:PersonUnderInvestigation ;
#    sh:property [
#        sh:path foaf:name ;
#        # Property is where things happen
#        sh:minCount 1 ; #Every person under investigation has exactly one name.
#        sh:maxCount 1 ; #Every person under investigation has exactly one name.
#        sh:datatype rdf:langString ; #All person names must be language-tagged
#    ] ;
#    # A SHACL string can have multiple properties targeting one class
#    :property [
#        :path :chargedWith ;
#        :nodeKind :URI ; #The object of a charged with property must be a URI.
#        :class :Offense ; #The object of a charged with property must be an offense.
#    ] .

# --- If you have more time tasks ---
# ex:MoreTime_Shape rdf:type sh:NodeShape;
#    sh:targetClass ex:Indictment;

# The only allowed values for ex:american are true, false or unknown.
#    sh:property [
#        sh:path ex:american;
#        sh:pattern "(true|false|unknown)" ;
#    ] ;
#
#    # The value of a property that counts days must be an integer.
#    sh:property [
#        sh:path ex:indictment_days;
#        sh:datatype xsd:integer;
#    ] ;