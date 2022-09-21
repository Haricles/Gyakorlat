'''
A mellékelt fájl néhány ismert programozási nyelv adatát tartalmazza. Olvasd be a fájl tartalmát és tárold el
a, egy listában, melynek elemei szótárak,
b, egy kétdimenziós listában!
mind a két esetben az évszám int típusként kerüljön rögzítésre!

(Fájl letöltése: kattints a "Forrásfájl" feliratú gombra az egér jobb gombjával, és a
felugró menüből válaszd a "Link mentése másként..." opciót!)
'''

#A feladat:
lista=[]
with open("Timeline_of_ programming_languages.txt","r",encoding="utf-8")as file:
    for sor in file:
        adatok=sor.strip().split(";")
        nyelvek={"Year":int(adatok[0]),
                 "Programming_languages":adatok[1],
                 "Fist Name":adatok[2],
                 "Last Name of chief developer":adatok[3]
                 }
        lista.append(nyelvek)
print (lista)

#B feladat:
lista_2=[]
with open("Timeline_of_ programming_languages.txt","r",encoding="utf-8")as file_2:
    for sor in file_2:
        adatok_2=sor.strip().split(";")
        ertek=[int(adatok_2[0]),adatok_2[1],adatok_2[2],adatok_2[3]]
        lista_2.append(ertek)
print (lista_2)

































