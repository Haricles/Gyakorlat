'''
Definiálja a maxElem(lista,kezdo,vegso) függvenyt ami a paraméterként átadott lista listából megadja a legnagyobb
értékű elemet. A kezdo és vegso argumentumokat adják meg az a két indexet amelyek között végre kell hajtani a keresést.
Közülük bármelyik elhagyható.

Példa: serie = [9,3,6,1,7,5,4,8,2]
print maxElem(serie)
9
print (maxElem(serie,2,5))
7
print ((maxElem(serie,2))
8
print (maxElem(serie,vegso=3,kezdo=1))
'''

lista= [9,3,6,1,7,5,4,8,2]
def maxElem(serie,kezdo=None,vegso=None):
    return (max(serie[kezdo:vegso]))

print (maxElem(lista))
print (maxElem(lista,2,5))
print (maxElem(lista,2))
print (maxElem(lista,vegso=3,kezdo=1))

