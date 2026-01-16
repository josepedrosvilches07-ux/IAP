temperatura = float(input("Pasam la temperatura"))
nuvolat = input("Esta nuvolat? (si/s)")

if nuvolat.lower() == "si" or nuvolat.lower() == "s":
    nuvolat == True
else:
    nuvolat == False


    if(temperatura<0):
        print("Fa un fred polar!")
    elif temperatura >0 and temperatura <=15 :
            if(nuvolat):
                 print("Fa fred i el dia esta trist.")
            else:
                 print("Fa fresquetaperò el sol alegra el dia.")