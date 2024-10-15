import json

file = open("pesate.json")
a = file.read()
file.close()

database = json.loads(a)

pesata = input("Inserisci pesata: ")

database.append(pesata)

b = json.dumps(database)

file = open("pesate.json", "w")
file.write(b)
file.close()