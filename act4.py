suma = 0
comptador_parells = 0

for i in range(1, 7):
    if i % 2 == 0:
        suma = suma + i
        comptador_parells = comptador_parells + 1
    else:
        suma = suma - 1

print("Resultat final:")
print("suma =", suma)
print("comptador_parells =", comptador_parells)

# i=    -   Condició    -   Suma    -   Parells
# ---------------------------------------------- 
# i=1   -   False       -   -1      -   0
# i=2   -   True        -    1      -   1
# i=3   -   False       -    0      -   1
# i=4   -   True        -    4      -   2
# i=5   -   False       -    3      -   2
# i=6   -   True        -    9      -   3