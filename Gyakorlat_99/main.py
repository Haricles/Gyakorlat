'''
Írj egy programot, amely generál egy véletlenszámot [1; 10] intervallumon, és a játékosnak ezt kell kitalálnia.
A próbálkozások száma nincs megkötve, de a program számolja a tippelési alkalmakat.

A program tartalmazzon
egy kitalalando nevű változót, ebben kerüljön tárolásra a generált véltelenszám,

egy tipp nevű változót, ez tárolja az éppen aktuális tippet,

egy main nevű függvényt, amely tartalmazza a főprogramot,

egy eltalalta nevű függvényt, amelynek
- 2 paramétere van, a játékos éppen aktuális tippje és az kitalálandó szám,
- visszatérési értéke True vagy False, attól függően,
hogy a paraméterként átvett értékek megegyeznek-e egymással vagy nem,

egy tipp_bekero nevű függvényt, amelynek
- nincs paramétere,
- bekéri a felhasználó tippjét, és azzal tér vissza.

'''
import random

def nem_talta(a,b):
    if a != b:
        return True
    else:
        return False

def tipp_bekero():
    a = int(input("kerek egy szamot:"))
    return a

def main():
    osszeg = 0
    kitalalando = random.randint(1, 10)
    tipp = 0
    while nem_talta(tipp,kitalalando):
        tipp = tipp_bekero()
        osszeg = osszeg + 1
    return "Tippek száma:",osszeg,"Kitalálandó szám: ",kitalalando

print(main())