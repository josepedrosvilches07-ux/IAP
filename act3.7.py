import csv

fitxer_oritge = "notes.csv"
fitxer_desti = "notes_modificat.csv"


dades_exemple = [
    ["Nom", "Assignatura", "Nota"],
    ["Sonia", "Programacio", "8"],
    ["Jose", "Seguretat", "7"],
    ["Paul", "Sistemes", "9"]
]

with open(fitxer_oritge, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(dades_exemple)

print(f"Fitxer '{fitxer_oritge}' creat per a la prova.\n")


dades_llegides = []

try:
    with open(fitxer_oritge, "r", newline="") as f:
        llegir = csv.reader(f)
        
        print("Contingut del fitxer original")
        for fila in llegir:
            print(fila)
            dades_llegides.append(fila)
    
    nom = input("Nom de l'alumne: ")
    assignatura = input("Assignatura: ")
    nota = input("Nota: ")
    
    nova_fila = [nom, assignatura, nota]
    
    dades_llegides.append(nova_fila)
    
    with open(fitxer_desti, "w", newline="") as f:
        escriure = csv.writer(f)
        escriure.writerows(dades_llegides)
        
    print(f"\nDades guardades correctament en '{fitxer_desti}'.")


except FileNotFoundError:
    print(f"El fitxer '{fitxer_oritge}' no existeix.")
except csv.Error as e:
    print(f"Fallada en processar el fitxer: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")