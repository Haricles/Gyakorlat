'''
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában.
Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában!
Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
'''

import random

lista=[]
for elem in range(1,6):
    a = random.randint(1,7)
    lista.append(a)

bemenet = int(input("Kerek egy szamot! "))

if bemenet in lista:
    print ("Benne van a listában")
else:
    print ("Nincs benne a listában.")

print (lista)











