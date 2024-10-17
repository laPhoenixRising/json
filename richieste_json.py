import requests
import json

request = requests.get('https://api.github.com/events')
data = json.loads(request.text)
# a = json.loads(content)
string = json.dumps(data, indent=2)
# b = json.dumps(a, indent=4)
file = open("salvataggio.json", "w")
file.write(string)
file.close()