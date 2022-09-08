'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja
el egy listában!
A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''

import random

lista = []
for elem in range(1,6):
    a = random.randint(1,10)
    lista.append(a)

osszeg = 0
for elem in lista:
    if elem % 2 == 0:
        osszeg = osszeg +1
print("A lista elemei: ",lista)
print ("A listában található páros számok száma:",osszeg)














