# 1 - Accedir a elements.

animals = ["gos", "gat", "conill", "lluç", "tortuga"]

print(animals[0])
print(animals[4])
print(animals[2])

# 2 - Modificar elements.

animals[2] = "salmó"
animals[3] = 5

print(animals)

# 3 - Mostrar tots els elements.

notes = [5, 7, 9, 4, 6, 3, 1, 8, 2, 10]
aprovats = 0
suspesos = 0

for nota in notes:
    print(nota)

for nota in notes:
    if nota >= 5:
        print(nota)

for nota in notes:
    if nota >= 5:
        aprovats = aprovats + 1
    else:
        suspesos = suspesos + 1

print(f"Hi han {aprovats} alumnes aprovats i {suspesos} alumnes suspesos.")

# 4 - Crear i modificar.

alumnes = []

alumnes.append("Jose")
alumnes.append("Carles")
alumnes.append("Pablo")
alumnes.append("Denis")
alumnes.append("Alex")

print(alumnes)