import json
import csv
import os
import shutil

fitxer_json = "estudiants.json"
fitxer_csv = "estudiants.csv"
carpeta_backup = "fitxers_antics"

if not os.path.exists(fitxer_json):
    dades_inicials = [
        {"nom": "Sonia", "edat": 21, "nota": 8.5, "assignatures": ["Xarxes", "Sistemes"]},
        {"nom": "Jose", "edat": 18, "nota": 7.0, "assignatures": ["Seguretat", "Aplicacions Web"]}
    ]
    with open(fitxer_json, "w") as f:
        json.dump(dades_inicials, f, indent=4)
    print("S'ha creat un fitxer JSON inicial de prova.\n")

print("GESTIÓ D'ESTUDIANTS")

try:
    print("1. Llegint dades del JSON...")
    with open(fitxer_json, "r") as f:
        llista_estudiants = json.load(f)
    
    print("\nAfegir nou estudiant")
    nom = input("Nom: ")
    edat = input("Edat: ")
    nota = input("Nota: ")
    assignatures_input = input("Assignatures: ")
    llista_assignatures = assignatures_input.split(",") 

    nou_estudiant = {
        "nom": nom,
        "edat": edat,
        "nota": nota,
        "assignatures": llista_assignatures
    }

    llista_estudiants.append(nou_estudiant)

    with open(fitxer_json, "w") as f:
        json.dump(llista_estudiants, f, indent=4)
    print(f"JSON actualitzat correctament.")

    if os.path.exists(fitxer_csv):
        print(f"\nEl fitxer CSV ja existeix. Movent a '{carpeta_backup}'...")
        
        if not os.path.exists(carpeta_backup):
            os.mkdir(carpeta_backup)
        
        desti = os.path.join(carpeta_backup, "estudiants_vell.csv")
        shutil.move(fitxer_csv, desti)
        print("Fitxer antic mogut correctament.")

    print("\nGenerant nou CSV...")
    with open(fitxer_csv, "w", newline="") as f:
        escriptor = csv.writer(f)
        
        escriptor.writerow(["Nom", "Edat", "Nota", "Assignatures"])
        
        for est in llista_estudiants:
            assignatures_str = "-".join(est["assignatures"])
            
            escriptor.writerow([est["nom"], est["edat"], est["nota"], assignatures_str])
            
    print(f"Nou fitxer '{fitxer_csv}' creat amb èxit.")

except FileNotFoundError:
    print("No s'ha trobat algun fitxer necessari.")
except json.JSONDecodeError:
    print("El fitxer JSON està corrupte.")
except PermissionError:
    print("No tens permisos.")
except Exception as e:
    print(f"Error INesperat: {e}")