'''
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot,
és ezeket tárolja el egy listában! A program adja össze a lista elemeit,
 írja ki a képernyőre az összegüket és a lista elemeit!

'''

import random
osszeg = 0
lista=[]
for elem in range(1,6):
    a = random.randint(1, 10)
    lista.append(a)
print (lista)


for elem in lista:
    osszeg = elem+osszeg
print (osszeg)





