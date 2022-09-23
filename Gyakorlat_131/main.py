'''
Készíts egy programot, amely egy-egy listában tárol 5 db egymástól különböző véletlenszámot [-5, 5] intervallumon!
A program írja ki a képernyőre a két lista elemeit, a két lista közös elemeit, valamint a két lista
összes elemét az esetleges ismétlődések mellőzésével!
'''

import random

lista_1=[]
lista_2=[]
for elem in range(0,5):
    random_szam=random.randint(-5,5)
    random_szam_2 = random.randint(-5, 5)
    lista_1.append(random_szam)
    lista_2.append(random_szam_2)
print (lista_1)
print (lista_2)

közös_elemek=[]
for elem in lista_1:
    if elem in lista_2:
        közös_elemek.append(elem)




print ("Közös elemek:",közös_elemek)
print ("Két lista összes eleme ismétlődés nélkül:",list(set(lista_1+lista_2)))
































































