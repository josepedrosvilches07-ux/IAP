import os

nom_fitxer = "prova.txt"

#1
f = open(nom_fitxer, "w")
f.write("Primera línia\n")
f.close()

f = open(nom_fitxer, "w")
f.write("Segona línia\n")
f.close()

#Al obrir el fitxer de nou en modo 'w', el contingut anterior ("Primera línia") es borra automáticament.
#El modo w sempre sobreescriu el fitxer desde cero; si había algo antes, es perd.


#2
try:
    f = open(nom_fitxer, "x")
    f.write("Tercera línia\n")
    f.close()
except FileExistsError:
    print("No es pot gastar 'x' perque el fitxer ja existeix.")

if os.path.exists(nom_fitxer):
    os.remove(nom_fitxer)

f = open(nom_fitxer, "x")
f.write("Tercera línia\n")
f.close()

#Python llança la excepció FileExistsError.
#Al no existir el fitxer, el modo 'x' funciona correctament,
#crea el archivo nou i escriu "Tercera línia".
#Este modo serveix per a asegurarse de que no sobreescribim res accidentalment.


#3
f = open(nom_fitxer, "a")
f.write("Cuarta línia\n")
f.close()


f = open(nom_fitxer, "a")
f.write("Quinta línia\n")
f.write("Sexta línia\n")
f.close()


f = open(nom_fitxer, "r")
print(f.read())
f.close()


#4
fitxer_falso = "no_existo.txt"
try:
    f = open(fitxer_falso, "r")
    contenido = f.read()
    f.close()
except FileNotFoundError:
    print(f"El fitxer '{fitxer_falso}' no existeix.")


    #Se obtiene la excepción FileNotFoundError.
    #Aço ocurreix per que el modo 'r' requereix obligatoriament que el fitxer existeixca previament.