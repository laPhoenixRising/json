import requests
import json

request = requests.get('https://api.github.com/events')
data = json.loads(request.text)
# print(type(data))
# print(len(data))
# print(type(data[6]))
# print(data[6].keys())
# section = data[6]
# print(position)
save = data[6]['repo']
# print(save)
string = json.dumps(save, indent=2)
file = open("salvataggio.json", "w")
file.write(string)
file.close()