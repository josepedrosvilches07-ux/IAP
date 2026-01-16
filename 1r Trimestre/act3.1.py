dades_usuari = "dades_usuari.txt"

try:
    nom = input("Introdueix el teu nom: ")
    edat = input("Introdueix la teua edat: ")

    with open(dades_usuari, "w") as f:
        f.write(f"Nom: {nom}\n")
        f.write(f"Edat: {edat}\n")
    

    with open(dades_usuari, "r") as f:
        fitxer = f.read()
        print(fitxer)

    ciutat = input("Introdueix la teua ciutat: ")

    with open(dades_usuari, "a") as f:
        f.write(f"Ciutat: {ciutat}\n")

    with open(dades_usuari, "r") as f:
        contenido_final = f.read()
        print(contenido_final)
    

except FileNotFoundError:
    print(f"ERROR: No s'ha trobat el fitxer {_}.")
except PermissionError:
    print("ERROR: No tens permisos per a escriure o llegir aquest fitxer.")
except Exception as e:
    print(f"Ha ocorregut un error inesperat: {e}")