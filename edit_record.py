import json

file = open("pesate.json")
a = file.read()
file.close()

database = json.loads(a)

index = int(input("Dimmi l'indice della pesata che vuoi modificare: "))

value = float(input("Inserisci nuovo valore: "))
database[index] = value

a = json.dumps(database)

file = open("pesate.json", "w")
file.write(a)
file.close()