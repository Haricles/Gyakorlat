'''
Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!
'''

import random
osszeg = 0
lista=[]
for elem in range(1,6):
    a = random.randint(1, 10)
    lista.append(a)
print (lista)


for elem in lista:
    if elem % 2 ==0:
        osszeg = elem+osszeg
print (osszeg)





