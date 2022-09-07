'''
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában.
 A végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista.
'''
import random


lista=[]
for elem in range(1,11):
    szamok = random.randint(0, 50)
    print (szamok)
    if szamok % 4 ==0:
        lista.append(szamok)

print("4-gyel osztható számok:",lista,"A lista ennyi elemből áll:",len(lista))





