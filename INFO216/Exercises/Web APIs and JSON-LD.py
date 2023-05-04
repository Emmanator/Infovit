import json, rdflib, requests, spotlight

r = requests.get('http://api.open-notify.org/astros.json')
r.encoding = 'utf-8'
json_r = r.json()

print(json_r['people'])

for i in json_r['people']:
    print(f'{i["craft"]}: {i["name"]}')
print(r.headers)
