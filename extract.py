import json
import random

with open("typhoon-names.txt","r") as f:
    lines = f.readlines()

data = {}
data['headers'] = lines[0]
data['rows'] = []
data['names'] = []
for line in lines[1:]:
    data['rows'].append(
        line.strip().split('\t')
        )

for row in data['rows']:
    for name in row[1:]:
        data['names'].append(name)

data['random-name'] = random.choice(data['names'])

print(json.dumps(data))