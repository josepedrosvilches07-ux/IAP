num = int(input("Introdueix un número: "))
cont = 0
while num != 0:
    cont += 1
    num = int(input("Introdueix un altre número: "))
    if num > 100:
        break
print(f"S'han introduït {cont} números positius.")