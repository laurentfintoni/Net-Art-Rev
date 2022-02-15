# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.artbase.rhizome.org/proxy/wdqs/bigdata/namespace/wdq/sparql"

query = """SELECT ?artwork_label ?description_label ?document_url {
  r:Q1292 rdfs:label ?artwork_label .
  r:Q1292 rt:P3 r:Q5 .
  r:Q1292 rt:P123 ?description .
  ?document_url schema:about ?description .
  ?description rdfs:label ?description_label .
}
LIMIT 100"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result['document_url']['value'], result['description_label']['value'])
