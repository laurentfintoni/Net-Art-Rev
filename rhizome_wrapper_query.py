# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.artbase.rhizome.org/proxy/wdqs/bigdata/namespace/wdq/sparql"

#query to get all artwork information

query = """SELECT ?artwork_page ?artwork_label ?artist_label ?accession ?inception ?summary_url ?description_url ?statement_url
{ 
  ?artwork rdfs:label ?artwork_label ;
   rt:P3 r:Q5 ;
   rt:P29 ?artist .
   ?artist rdfs:label ?artist_label . 
   ?artwork_page schema:about ?artwork .
  OPTIONAL {
   ?artwork rt:P85 ?accession ;
           rt:P26 ?inception . }
  OPTIONAL {
  ?artwork rt:P123 ?summary_description .
  ?summary_description rt:P3 r:Q4985 ;
          rdfs:label ?summary_label .
  ?summary_url schema:about ?summary_description .}
  OPTIONAL {
  ?artwork rt:P123 ?description .
  ?description rt:P3 r:Q9759 ;
          rdfs:label ?description_label .
  ?description_url schema:about ?description . }
  OPTIONAL {
    ?artwork rt:P123 ?statement .
  ?statement rt:P3 r:Q11838 ;
          rdfs:label ?statement_label .
  ?statement_url schema:about ?statement .
}}

"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)


  """ 
#artists unique no collectives + person that are members of a collective
SELECT DISTINCT ?artistLabel ?member ?artistPage ?collective
WHERE {
?artwork rt:P3 r:Q5.
?artwork rt:P29 ?artist.
?artist rt:P3 r:Q6.
?artistPage schema:about ?artist ;
schema:isPartOf <https://artbase.rhizome.org/> .
?collective rt:P3 r:Q7;
rt:P43 ?member.
SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
FILTER (?artist not in (r:Q7) )
}
ORDER BY ?artistLabel
}

#filter out collectives from the unqiue artists query --> artists unique no collectives
SELECT DISTINCT ?artistLabel ?artistPage
WHERE {
?artwork rt:P3 r:Q5.
?artwork rt:P29 ?artist.
?artist rt:P3 r:Q6.
?artistPage schema:about ?artist ;
schema:isPartOf <https://artbase.rhizome.org/> .
SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
FILTER (?artist not in (r:Q7) )
}
ORDER BY ?artistLabel
}
  """