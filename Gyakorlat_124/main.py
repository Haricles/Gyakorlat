'''
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát,
és másold át azt egy fájlba úgy, hogy abba már csak a nyelv és az évszám kerüljön!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával,
és a felugró menüből válaszd a "Link mentése másként..." opciót!)

'''
with open("Timeline_of_ programming_languages.txt","r",encoding="utf-8") as bemenet:
    with open("masolat.txt","w",encoding="utf-8") as kimenet:
        for elem in bemenet:
            adat=elem.strip()
            adat_2= adat.split(";")
            kimenet.write("\n"+adat_2[0]+"\t"+adat_2[1])





























