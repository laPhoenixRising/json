import json

file = open("pesate.json")
a = file.read()
file.close()

database = json.loads(a)

print(database)

index = int(input("Dammi l'indice della pesata che vuoi cancellare: "))
database.pop(index)

print(database)

a = json.dumps(database)

file = open("pesate.json", "w")
file.write(a)
file.close()