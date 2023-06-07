from pyshacl import validate
from rdflib import Graph

data_graph = Graph()
# parses the Turtle examples from the lab
data_graph.parse("data_graph.ttl")

# Remember to test you need to change the rules so they conflict with the data graph (or vice versa). For example, change "exactly one name" to have exactly two, and see the output
shape_graph = """
@prefix ex: <http://example.org/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:LabTasks_Shape
    a sh:NodeShape ;
    sh:targetClass ex:PersonUnderInvestigation ;
    sh:property [
        sh:path foaf:name ;
        sh:minCount 1 ; #Every person under investigation has exactly one name. 
        sh:maxCount 1 ; #Every person under investigation has exactly one name.
        sh:datatype rdf:langString ; #All person names must be language-tagged
    ] ;
    sh:property [
        sh:path ex:chargedWith ;
        sh:nodeKind sh:IRI ; #The object of a charged with property must be a URI.
        sh:class ex:Offense ; #The object of a charged with property must be an offense.
    ] .

# --- If you have more time tasks ---
ex:MoreTime_Shape rdf:type sh:NodeShape;
    sh:targetClass ex:Indictment;

    # The only allowed values for ex:american are true, false or unknown.
    sh:property [
        sh:path ex:american;
        sh:pattern "(true|false|unknown)" ;
    ] ;

    # The value of a property that counts days must be an integer.
    sh:property [
        sh:path ex:indictment_days;
        sh:datatype xsd:integer;
    ] ;   
    sh:property [
        sh:path ex:investigation_days;
        sh:datatype xsd:integer;
    ] ;

    # The value of a property that indicates a start date must be xsd:date.
    sh:property [
        sh:path ex:investigation_start;
        sh:datatype xsd:date;
    ] ;

    # The value of a property that indicates an end date must be xsd:date or unknown (tip: you can use sh:or (...) ).
    sh:property [
        sh:path ex:investigation_end;
        sh:or (
         [ sh:datatype xsd:date ]
         [ sh:hasValue "unknown" ]
    )] ;

    # Every indictment must have exactly one FOAF name for the investigated person.
    sh:property [
        sh:path foaf:name;
        sh:minCount 1;
        sh:maxCount 1;
    ] ;

    # Every indictment must have exactly one investigated person property, and that person must have the type ex:PersonUnderInvestigation.
    sh:property [
        sh:path ex:investigatedPerson ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:class ex:PersonUnderInvestigation ;
        sh:nodeKind sh:IRI ;
    ] ;

    # No URI-s can contain hyphens ('-').
    sh:property [
        sh:path ex:outcome ;
        sh:nodeKind sh:IRI ;
        sh:pattern "^[^-]*$" ;
    ] ;

    # Presidents must be identified with URIs.
    sh:property [
        sh:path ex:president ;
        sh:class ex:President ;
        sh:nodeKind sh:IRI ;
    ] .
"""

shacl_graph = Graph()
# parses the contents of a shape_graph made in the tasks
shacl_graph.parse(data=shape_graph)

# uses pySHACL's validate method to apply the shape_graph constraints to the data_graph
results = validate(
    data_graph,
    shacl_graph=shacl_graph,
    inference='both'
)

# prints out the validation result
boolean_value, results_graph, results_text = results

# print(boolean_value)
print(results_graph.serialize(format='ttl'))
# print(results_text)

# Write a SPARQL query to print out each distinct sh:resultMessage in the results_graph
distinct_messages = """
PREFIX sh: <http://www.w3.org/ns/shacl#> 

SELECT DISTINCT ?message WHERE {
    [] sh:result ?errorBlankNode.
    ?errorBlankNode sh:resultMessage ?message.    

    # Alternativ and cleaner solution, look at https://www.w3.org/TR/sparql11-query/#pp-language (9.1 Property Path Syntax)
    # [] sh:result / sh:resultMessage ?message .
}
"""
messages = results_graph.query(distinct_messages)
for row in messages:
    print(row.message)

# each sh:resultMessage in the results_graph once, along with the number of times that message has been repeated in the results
count_messages = """
PREFIX sh: <http://www.w3.org/ns/shacl#> 

SELECT ?message (COUNT(?node) AS ?num_messages) WHERE {
    [] sh:result ?errorBlankNode .
    ?errorBlankNode sh:resultMessage ?message ;
                    sh:focusNode ?node .
}
GROUP BY ?message
ORDER BY DESC(?count) ?message
"""

messages = results_graph.query(count_messages)
for row in messages:
    print(f"COUNT: {row.num_messages} | MESSAGE: {row.message}")
