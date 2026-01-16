llista_fitxers = ["dades_usuari.txt", "arxiu_inventat.txt", "altre_fitxer.txt"]

fitxer_desti = "fitxer_concatenat.txt"

try:
    with open(fitxer_desti, "w") as f_salida:
        
        for nom_actual in llista_fitxers:
            
            try:
                with open(nom_actual, "r") as f_entrada:
                    contingut = f_entrada.read()
                    
                    f_salida.write(contingut)
                    f_salida.write("\n\n")
                    
            
            except FileNotFoundError:
                print(f"El fitxer '{nom_actual}' no existeix. S'ha omitit.")
            except PermissionError:
                print(f"No tens permis per a llegir '{nom_actual}'.")


except Exception as e:
    print(f"Ha ocorregut un error general: {e}")