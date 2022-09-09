'''
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista
legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!

'''


lista_1 = []
bemenet = 1
while bemenet > 0:
    bemenet = int(input("Kerek egy számot: "))
    if bemenet > 0:
        lista_1.append(bemenet)
print (lista_1)

def legkisebb(lista):
    return min(lista)

print (legkisebb(lista_1))






