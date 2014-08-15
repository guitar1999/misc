#!/usr/bin/python
import json
f = open('sessionstore.js', 'r')
json_string = f.read()
parsed_json = json.loads(json_string)
p = parsed_json['lastSessionState']['windows'][0]
for t in p['tabs']:
    for e in t['entries']:
        print e['url']

