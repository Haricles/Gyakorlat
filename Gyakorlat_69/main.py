'''
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát
írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje
 ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
'''
import random

a = 1
lista = []
while a <= 10:
    b = random.randint(1,3)
    lista.append(b)
    a+= 1
print (lista)
h = int(input("Kerek egy szamot: "))
for elem in lista:
    if h in lista:
        lista.remove(h)
print (lista)





