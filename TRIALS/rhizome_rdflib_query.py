import rdflib
import pprint

# create an empty Graph
g = rdflib.ConjunctiveGraph()

# parse a local RDF file by specifying the format
result = g.parse("Rhizome_data/Rhizome-ArtBase_2022-02-14.ttl", format="ttl")

query_results = g.query(
    """SELECT ?artwork_page ?artwork_label ?artist_label ?accession ?inception ?summary_url ?description_url ?statement_url
{ 
  ?artwork rdfs:label ?artwork_label ;
   wdt:P3 wd:Q5 ;
   wdt:P29 ?artist .
   OPTIONAL {
   ?artwork wdt:P85 ?accession ;
           wdt:P26 ?inception .}
  OPTIONAL {
  ?artist rdfs:label ?artist_label .}
  OPTIONAL {
  ?artwork_page schema:about ?artwork .}
  OPTIONAL {
  ?artwork wdt:P123 ?summary_description .}
  OPTIONAL {
  ?summary_description wdt:P3 wd:Q4985 ;
          rdfs:label ?summary_label .}
  OPTIONAL {
  ?summary_url schema:about ?summary_description .}
  OPTIONAL {
  ?artwork wdt:P123 ?description .
  ?description wdt:P3 wd:Q9759 ;
          rdfs:label ?description_label .}
  OPTIONAL {
  ?description_url schema:about ?description .}
  OPTIONAL {
    ?artwork wdt:P123 ?statement .
  ?statement wdt:P3 wd:Q11838 ;
          rdfs:label ?statement_label .}
  OPTIONAL {
  ?statement_url schema:about ?statement .}
}""")

for query_res in query_results:
  print(query_res) # notice the two alternative ways to recall values in the tuple