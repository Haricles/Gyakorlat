'''
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy
eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!


'''

lista_01= []

for elem in range(1,4):
    a = input("Kerek 3 szót! ")
    lista_01.append(a)
print (lista_01)

def legrövidebb(lista):
    a = lista[0]
    for elem in lista:
        if len(a) > len(elem):
            a = elem
    print (a)

legrövidebb(lista_01)












