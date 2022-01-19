#!!!!!!!!! Incomplete !!!!
# WIP

import json
import requests
from elasticsearch import Elasticsearch

res = requests.get('http://localhost:9200')
print(res.content)

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

filename = 'input.json'
f = open(filename)
# json_content = '['+f.read().strip()[:-1]+']'
json_content = f.read()
#print(json_content)

# Send the data into es
es.index(index='db', ignore=400, document=json.loads(json_content))
# es.bulk(index='db', json_content)
