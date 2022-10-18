'''
Krisztián szeretne statisztikát készíteni a Dokumentumok mappájában található fájlokról,
ezért egy Python szkriptet ír. A szkript feladata, hogy megszámolja, hogy az adott mappán belül mennyi
található a különböző kiterjesztésekből. A program egy részét Krisztián már megírta,
viszont a statisztika-készítésben kellene neki egy kis segítség.

Írj egy statisztika nevű függvényt, amely egy listát kap paraméterül!
A lista fájlok neveit tartalmazza, kiterjesztéssel együtt. A fájlnévben a kiterjesztés alatt a legutolsó
pont karakter után lévő szöveget értjük. A függvény számolja meg, hogy az egyes kiterjesztések hányszor
fordulnak elő a listában, és az eredményt adja vissza egy dictionary-ben, a példában látható formátumban!

A feladatot úgy oldd meg, hogy a kiterjesztés vizsgálata során ne különböztesd meg a kis- és nagybetűket
(tehát pl. hello.py és WORLD.PY egyaránt py kiterjesztésűek).
Input: ['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']
Return: {'py': 3, 'java': 1, 'mp4': 2}
'''
def statisztika(lista):
    szamlalok=[0]*3
    szotar = {}
    for szavak in lista:
        szo_lista=szavak.split(".")
        for elem in szo_lista:
            if elem.lower() == "py":
                szamlalok[0]+=1
            if elem.lower() =="mp4":
                szamlalok[1]+=1
            if elem.lower()=="java":
                szamlalok[2]+=1
    szotar["py"]=szamlalok[0]
    szotar["mp4"]=szamlalok[1]
    szotar["java"]=szamlalok[2]
    return szotar

fajlok_nevei=['feladat.py', 'Bolygo.java', 'HELLOFRIENDS.MP4', 'TEST.PY', 'biro.gib.maxpont.py', 'russian-driving-fails.mp4']
print (statisztika(fajlok_nevei))
