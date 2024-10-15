import json

file = open("pesate.json")
a = file.read()
file.close()

nuovo_file = json.loads(a)

pesata = input("Inserisci pesata: ")

nuovo_file.append(pesata)

b = json.dumps(nuovo_file)

file = open("pesate.json", "w")
file.write(b)
file.close()