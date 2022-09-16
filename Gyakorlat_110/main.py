'''
Készíts egy programot, amely egy kétdimenziós listában tárol ötször három darab véletlenszámot [-5;5] intervallumon.
A program írja ki a kétdimenziós lista elemeit, majd fésülje át a lista tartalmát és törölje belőle a negatív számokat.
Végül ismét kerüljön kiírásra lista tartalma!
'''
import random

lista=[[],[],[],[],[]]
for elem in range(5):
    for i in range(3):
        random_szam= random.randint(-5,5)
        lista[elem].append(random_szam)
print (lista)

result= []
for k in lista:
    tmp=[elem for elem in k if elem>0]
    result.append(tmp)
print(result)




