import json

x = {"Name": "Alex", "City": "Maracanau", "Idade": 23}
y = json.dumps(x) # Converte dados python para json
# y = json.loads(x) # Converte dados json para python
print(y["Name"])