import json

list = []

list_json = json.dumps(list)

file = open("pesate.json", "w")
file.write(list_json)
file.close()

