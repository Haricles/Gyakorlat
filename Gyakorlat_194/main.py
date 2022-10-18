'''
Egy baráti társaság a népszerű skribbl.io játékkal játszik.
A játék minden körében egy játékos lerajzol egy előre megadott dolgot, amit a többiek megpróbálnak kitalálni.
Az egyes körök során a játékosok pontokat gyűjtenek.

Írj egy vegeredmeny nevű függvényt, amely egy dictionary-kből álló listát kap paraméterül!
A dictionary-k az egyes körök eredményeit tartalmazzák: a kulcsok a játékosok nevei, az
értékek pedig az adott körben a játékos által elért pontszám. A függvény összesítse játékosonként a pontokat,
és az így kapott összesítést adja vissza egy dictionary-ben, a példában látható formátumban!
Input:
[
  { 'shronk': 400, 'Tamas': 200, 'adam': 800, 'Wolf': 500, 'Karoly': 70 },
  { 'Tamas': 0, 'Wolf': 0, 'Karoly': 200, 'shronk': 0, 'adam': 100 },
  { 'Wolf': 600, 'adam': 400, 'Karoly': 500, 'shronk': 200, 'Tamas': 300 },
  { 'Tamas': 500, 'Wolf': 100, 'Karoly': 0, 'shronk': 600, 'adam': 200 },
  { 'adam': 100, 'Wolf': 500, 'shronk': 0, 'Tamas': 300, 'Karoly': 100 }
]

Return: {'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}
'''
#1.megolas
def vegeredmeny(lista):
    eredmeny={}
    for elem in lista:
        for key,value in elem.items():
            if key not in eredmeny:
                eredmeny[key]=value
            else:
                eredmeny[key]+=value
    return eredmeny

#2.megoldás
def vegeredmeny_2(lista):
    szamlalok=[0]*5
    for elem in lista:
        if elem["shronk"]:
            szamlalok[0]+=elem["shronk"]
        if elem["Tamas"]:
            szamlalok[1] += elem["Tamas"]
        if elem["adam"]:
            szamlalok[2] += elem["adam"]
        if elem["Wolf"]:
            szamlalok[3] += elem["Wolf"]
        if elem["Karoly"]:
            szamlalok[4] += elem["Karoly"]
    uj_szotar={'shronk': szamlalok[0], 'Tamas': szamlalok[1], 'adam': szamlalok[2], 'Wolf': szamlalok[3], 'Karoly': szamlalok[4]}
    return uj_szotar

bemenet=[
  { 'shronk': 400, 'Tamas': 200, 'adam': 800, 'Wolf': 500, 'Karoly': 70 },
  { 'Tamas': 0, 'Wolf': 0, 'Karoly': 200, 'shronk': 0, 'adam': 100 },
  { 'Wolf': 600, 'adam': 400, 'Karoly': 500, 'shronk': 200, 'Tamas': 300 },
  { 'Tamas': 500, 'Wolf': 100, 'Karoly': 0, 'shronk': 600, 'adam': 200 },
  { 'adam': 100, 'Wolf': 500, 'shronk': 0, 'Tamas': 300, 'Karoly': 100 }
]

print (vegeredmeny(bemenet))
print(vegeredmeny_2(bemenet))