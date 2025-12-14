print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 0

while i < n:
    nom = input("Nom: ")
    edat = int(input("Edat: "))
    assist = input("Assistència (S/N): ").lower()

    if edat < 12:
        categoria = "infantil"
    elif edat > 12 and edat < 18:
        categoria = "adolescent"
    elif edat >= 18 and edat < 65:
        categoria = "adult"
    else:
        categoria = "jubilat"

    if assist.lower() == "s" or "si":
        estat = "present"
    else:
        estat = "absent"

    print(nom, "-", categoria, "-", estat)
    i = i + 1