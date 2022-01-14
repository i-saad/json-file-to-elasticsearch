import requests, json, os
from elasticsearch import Elasticsearch

# ping to check status and access to es
res = requests.get('http://localhost:9200')
print (res.content)

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

filename = 'input.json'
with open(filename, "r") as a_file:
  for line in a_file:
    json_content = line.strip()[:-1]
    #print(json_content)

    # Send the data into es
    es.index(index='db', ignore=400, body=json.loads(json_content))
