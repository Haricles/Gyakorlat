'''
Fejlesszük tovább a 2.3 programot úgy, hogy a program egy listában tároljon öt darab szót, és abból véletlenszerűen
válasszon egyet, aminek kapcsán a felhasználó megpróbálja kitalálni a betűit.
'''

import random

lista = ["alma","körte","szilva","szőlő","mák"]

a = random.choice(lista)
bemenet = None
tipp_jo = ""
tipp_rossz = ""

while bemenet != "":
    bemenet = input("Kerek egy betüt: ")
    if bemenet != "":
        if bemenet in a:
            tipp_jo = bemenet + tipp_jo
            print ("Benne van!")

        else:
            tipp_rossz = bemenet + tipp_rossz
            print ("Nincs benne!")


print ("A tárolt szó:",a)
print ("Eltalált betűk:",tipp_jo,"Elvétett betűk:",tipp_rossz)











