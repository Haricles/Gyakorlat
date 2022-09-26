'''
Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
a megadott szám értéke!
'''
szam = 0
while True:
    szam = int(input("Kerek egy számot: "))
    if szam > 0 or szam < 20:
        sor = ""
        for i in range(szam):
            sor += " "
        print (sor + "START")




















