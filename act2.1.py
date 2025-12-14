temperatura = float(input("Pasam la temperatura"))
nuvolat = input("Esta nuvolat? (si/s)")

if nuvolat.lower() == "si" or nuvolat.lower() == "s":
    nuvolat = True
else:
    nuvolat = False


if(temperatura<=0):
       print("Fa un fred polar!")
elif temperatura >0 and temperatura <=15:
       if(nuvolat):
                 print("Fa fred i el dia esta trist.")
       else:
                 print("Fa fresquetaperò el sol alegra el dia.")
elif temperatura >=16 and temperatura <=25:
       if(nuvolat):
                 print("Temperatura agradable, però potser ploga.")
       else:
                 print("Dia perfecte per eixir a passejar!")
elif temperatura >=26 and temperatura <=35:
       print("Fa calor, millor buscar ombra.")
elif temperatura >35:
       if(nuvolat):
                 print("Calor i humitat... una combinació infernal!")
       else:
                 print("Fa una calor que fon les pedres!")