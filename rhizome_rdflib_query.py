import rdflib
import pprint

# create an empty Graph
g = rdflib.ConjunctiveGraph()

# parse a local RDF file by specifying the format
result = g.parse("Rhizome_data/Rhizome-ArtBase_2022-02-14.ttl", format="ttl")

query_results = g.query(
    """SELECT ?artwork_label ?description_label ?document_url {
  wd:Q1292 rdfs:label ?artwork_label .
  wd:Q1292 wdt:P123 ?description .
  ?document_url schema:about ?description .
  ?description rdfs:label ?description_label .
}
LIMIT 100""")

for query_res in query_results:
  print(query_res) # notice the two alternative ways to recall values in the tuple