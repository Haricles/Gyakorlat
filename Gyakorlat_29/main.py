'''
Definiáljon egy maximum(n1,n2,n3) függvényt,ami az arugmentumként megadott n1,n2,n3 számok közül a a legnagyobbat
adja vissza. pl: print maximum(2,5,4) utasítás végrehajtásakor 5-t kell kapnunk.
'''
#1. megoldás:
def maximum(n1,n2,n3):
    return max(n1,n2,n3)

print (maximum(2,5,4))

#2. megoldás:

def maximum_2(n1,n2,n3):
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem
    return legnagyobb

print (maximum_2(8,9,7))

# 3.megoldas:
def maximum_3(n1,n2,n3):
    legnagyobb = n1
    for elem in n1,n2,n3:
        if elem > legnagyobb:
            legnagyobb= elem
    return legnagyobb

print (maximum_3(6,7,9))