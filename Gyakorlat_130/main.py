'''
Készíts egy programot, amely generál és listában tárol 10 darab véletlenszámot [-20;20] inetrvallumon,
kírja a lista elemeit, majd megjeleníti azokat növekvő sorrendben is! A lista rendezését saját magad által
megírt algoritmus végezze buborék rendezés módszerével! Ezen a honlapon tudod megnézni a
buborékrendezés működését és pszeudókódját.

'''

import random

lista=[]
for elem in range(0,10):
    random_szam=random.randint(-20,20)
    lista.append(random_szam)
print ("Alap lista:",lista)

for elem in range(len(lista)-1):
    for mogotte in range(elem+1,len(lista)):
        if lista[elem] > lista[mogotte]:
            lista[elem],lista[mogotte] = lista[mogotte],lista[elem]
print ("Növekvő sorrend:",lista)






































































