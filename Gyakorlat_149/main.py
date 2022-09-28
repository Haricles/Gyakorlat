'''
Írjon egy  karakterszam()  függvényt, ami megszámolja, hogy egy karakter hányszor fordul elő egy
stringben. Így a következő utasításnak 4-et kell kiírni :
print karakterszam("ananas au jus","a")

'''
#1.megoldás:
def karakterszam(sztring,karakter):
    return sztring.count(karakter)


print (karakterszam("ananas au jus","a"))


#2.megoldás:
def karakterszam_2(sztring,karakter):
    i =0
    for elem in sztring:
        if elem == karakter:
            i +=1
    return i

print (karakterszam_2("ananas au jus","a"))





































