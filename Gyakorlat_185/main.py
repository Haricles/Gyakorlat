'''
Írj egy leghosszabb_szo nevű függvényt, amely egy szöveget kap paraméterül
(a szöveg szóközzel elválasztott szavakat tartalmaz)! A függvény térjen vissza a szövegben található leghosszabb szóval!
Amennyiben több szó is ugyanolyan hosszú, akkor közülük a szövegben korábban előfordulót add vissza!

Ha a paraméterül kapott szöveg az üres string, akkor a visszatérési érték a HIBA! szöveg legyen!

Input: 'Szia uram! Mondd mar meg, hogy hany ora van!'
Return: 'uram!'

Input: ''
Return: 'HIBA!'
'''


def leghosszabb_szo(szoveg):
    if szoveg == "":
        return "HIBA"
    lista=bemenet.split()
    leghosszabb = lista[0]
    for elem in lista:
        if len(leghosszabb)< len(elem):
            leghosszabb=elem
    return leghosszabb

bemenet = "Szia uram! Mondd mar meg, hogy hany ora van!"
bemenet_2=""
print (leghosszabb_szo(bemenet))
print (leghosszabb_szo(bemenet_2))