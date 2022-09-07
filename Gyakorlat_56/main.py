'''
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa
a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére,
írja ki az addig megadott neveket, és lépjen ki.

'''
nevek = []
szamlalo = 1
nev = None
while nev != "":
    nev = input("Kerem a neved: ")
    if nev != "":
        nevek.append(nev)
    if szamlalo == 3:
        print("Már nem tudsz több nevet hozzáadni.","Eddigi nevek: ",nevek)
        quit()
    szamlalo +=1
print (nevek)




