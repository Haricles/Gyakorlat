'''
Írjon egy függvényt, amivel rendezni lehet egy listát. A függvény ne használja a Python beépített sort()
metódusát : tehát egy rendezési algoritmust kell definiálni.

'''
lista=[3,6,2,9,8,45,1,76,5]

for elem in range(len(lista)-1):
    for mogotte in range(elem+1,len(lista)):
        if lista[elem] > lista[mogotte]:
            lista[elem],lista[mogotte]=lista[mogotte],lista[elem]

print (lista)

