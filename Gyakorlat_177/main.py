'''
Módosítsa az előbbi scriptet úgy, hogy a szövegben előforduló szavakból hozzon létre egy táblázatot.
Észrevétel :   a   szövegekben   a   szavakat   nemcsak   betűközök,   hanem   írásjelek   is   elválaszthatják
egymástól.   A   probléma   egyszerűsítése   érdekében   kezdhetjük   az   összes   nem   alfabetikus   karakter
betűközzel   való   helyettesítésével,   majd   az   eredménystringet   a  split()  metódussal   átalakíthatjuk
szavakból álló listává.
'''

uj=""
irasjelek=[",",".","?","!"]
with open("bemenet.txt","r",encoding="utf-8") as file:
    for i in file:
        sor = i
        for elem in sor:
            if elem in irasjelek:
                elem = ""
                uj +=elem
            else:
                uj +=elem
lista= uj.split()
print(lista)





