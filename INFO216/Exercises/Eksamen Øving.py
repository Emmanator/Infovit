from rdflib import RDF, RDFS, FOAF, OWL, Namespace, Graph, XSD, Literal

g = Graph()

ex = Namespace('http://ex.org#')

g.add((ex.Agent, RDF.type, OWL.Class))
g.add((ex.Publication, RDF.type, OWL.Class))

g.add((ex.Author, RDFS.subClassOf, ex.Agent))
g.add((ex.Organization, RDFS.subClassOf, ex.Agent))
g.add((ex.Country, RDFS.subClassOf, ex.Agent))
g.add((ex.Paper, RDFS.subClassOf, ex.Publication))

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

g.add((ex.the_semantic_web, RDF.type, ex.Paper))
g.add((ex.the_semantic_web, ex.title, Literal("The Semantic Web")))
g.add((ex.the_semantic_web, ex.author, ex.Tim_Berners_Lee))
g.add((ex.the_semantic_web, ex.author, ex.James_Hendler))
g.add((ex.the_semantic_web, ex.publication, ex.Scientific_American))
g.add((ex.the_semantic_web, ex.publisher, ex.Springer_Nature))
g.add((ex.the_semantic_web, ex.year, Literal(2001)))

g.add((ex.Tim_Berners_Lee, RDF.type, ex.Author))
g.add((ex.Tim_Berners_Lee, ex.name, Literal("Tim Berners Lee")))
g.add((ex.Tim_Berners_Lee, ex.affiliation, ex.MIT))
g.add((ex.Tim_Berners_Lee, ex.country, ex.United_States))

# :Organization rdfs:subClassOf :Agent .
# :affiliation rdfs:range :Organization
# :affiliation rdfs:domain :Author
# :publication owl:cardinality 1
# :publication rdf:type owl:FunctionalProperty
# :year owl:maxCardinality 1
# :publication rdf:type owl:IrreflexiveProperty
# :publication rdf:type owl:TransitiveProperty
# :name rdf:type owl:InverseFunctionalProperty
# :Author owl:disjointWith :Organization
# :title rdfs:range xsd:string
#
# :Paper rdfs:subClassOf [ rdf:type owl:Restriction ;
#                          owl:minCardinality "1" ;
#                          owl:onProperty :author
#                        ] .
#
# :Paper rdfs:subClassOf [ rdf:type owl:Restriction ;
#                          owl:cardinality "1" ;
#                          owl:onProperty :title
#                        ] .
#
# :year rdfs:range [ rdf:type owl:DataRange ;
#                    owl:minInclusive "1900" ;
#                    owl:maxInclusive "2050"
#                  ] .

# :Author owl:disjointWith :Organization
# :Author owl:disjointWith :Country
# :Organization owl:disjointWith :Country
#
# :Publisher owl:oneOf (:CM :IEEE_CS :Springer_Nature :IGI_Global)
#

# SELECT ?title
# WHERE {
# ?paper rdf:type :Paper ;
#   :title ?title .
# }

# SELECT DISTINCT ?name
# WHERE {
#   ?p rdf:type :Publication ;
#       :publisher / :name ?name
# }
# ORDER BY ?name

# SELECT ?name ?title
# WHERE {
#   ?author ^:name / ^:author / :title ?title
#
#   ?p :author ?a .
#   ?p rdf:type :Paper .
#   ?p :title ?title .
#   ?a :name ?name
# }

# SELECT ?c (COUNT(?p) AS ?number)
# WHERE {
# ?p rdf:type :Paper ;
#   :author / :country / :name ?c
# }
# GROUP BY ?c

# SELECT ?a (COUNT(?p) AS ?number)
# WHERE {
# ?p rdf:type :Paper ;
#   :author / :name ?a
# }
# GROUP BY ?a
# ORDER BY ?number DESC

# SELECT ?a (MIN(?y) as ?min) (MAX(?y) as ?max)
# WHERE {
#   ?p rdf:type :Paper ;
#       :year ?y ;
#       :author / :name ?a
# }
# GROUP BY ?a

# SELECT ?name
# WHERE {
#   ?a rdf:type :Author ;
#       :name ?name
#   MINUS {
#       ?a :affiliation / :country / :name "Germany"
#   }
# }

# ASK {
#   ?a rdf:type :Author ;
#       :name "James Hendler" .
#   ?p1 :author ?a .
#   ?p2 :author ?a .
#   FILTER (?p1 != ?p2)
# }

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

# INSERT {
#   ?org rdf:type :Institution
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?org
# }

# INSERT {
#   ?org :locatedIn ?country
# } WHERE {
#   ?a rdf:type :Author ;
#       :country ?country ;
#       :affiliation ?org
# }

# INSERT {
#   ?p :producedBy ?org
# } WHERE {
#   ?a rdf:type :Author ;
#       :affiliation ?org ;
#       ^:author ?p
# }

# INSERT {
#   ?p :producedIn ?c
# } WHERE {
#   ?p rdf:type :Paper ;
#       :author / :affiliation / :locatedIn ?c
# }

# DELETE {
#   ?a :country ?c
# } WHERE {
#   ?a :country ?c
# }

# DELETE {
#   ?p :year ?y2
# } WHERE {
#   ?p rdf:type :Paper ;
#       :year ?y1 ;
#       :year ?y2 
#   FILTER(?y1 < ?y2)
# }

#ex:LabTasks_Shape
#    a sh:NodeShape ;
#    sh:targetClass ex:PersonUnderInvestigation ;
#    sh:property [
#        sh:path foaf:name ;
#        sh:minCount 1 ; #Every person under investigation has exactly one name.
#        sh:maxCount 1 ; #Every person under investigation has exactly one name.
#        sh:datatype rdf:langString ; #All person names must be language-tagged
#    ] ;
#    sh:property [
#        sh:path ex:chargedWith ;
#        sh:nodeKind sh:IRI ; #The object of a charged with property must be a URI.
#        sh:class ex:Offense ; #The object of a charged with property must be an offense.
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