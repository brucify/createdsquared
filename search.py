"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib
import sys

api_key = open('.api_key').read()
query = str(sys.argv[1])
print "Searching term: " + query + "..."
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.urlencode(params)
response = json.loads(urllib.urlopen(url).read())
#for element in response['itemListElement']:
#  print element['result']['name'] + ' (' + str(element['resultScore']) + ')'
print json.dumps(response, sort_keys=True, indent=4)
