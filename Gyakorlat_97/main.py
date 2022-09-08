'''
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában,
és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)


'''
mylist=[]
bemenet = 1
while bemenet > 0:
    bemenet = int(input("Kerek egy szamot: "))
    if bemenet > 0:
        mylist.append(bemenet)
print (mylist)

def harommal_oszthatok(lista):
    osszeg = 0
    for elem in lista:
        if elem % 3 == 0:
            osszeg = osszeg +1
    return osszeg

print (harommal_oszthatok(mylist))





