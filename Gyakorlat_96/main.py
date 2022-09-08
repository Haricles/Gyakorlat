'''
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában
megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!


'''
mylist=[9,53,3,7,9,2,4,15,5,6,3,12]

def harommal_oszthatok(lista):
    osszeg = 0
    for elem in lista:
        if elem % 3 == 0:
            osszeg = osszeg +1
    return osszeg

print (harommal_oszthatok(mylist))





