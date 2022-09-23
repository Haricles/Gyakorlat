'''
Készíts egy programot, ami a felhasználó által megadott intervallumon állít elő szintén a felhszanáló által megadott
darab véletlen egész számot! Ezeket a program írja ki a képernyőre emelkedő és csökkenő sorrendben!
'''
import random

a= int(input("Kerem a kezdet: "))
b = int(input("Kerem a végét: "))
n = int(input("Kerem hány db véletlen szám legyen! "))

lista=[]
for elem in range(n):
    random_szam= random.randint(a,b)
    lista.append(random_szam)
rendezes_novekvo=(sorted(lista))
rendezes_csokkeno=(sorted(lista,reverse=True))



print (lista)
print (rendezes_novekvo)
print (rendezes_csokkeno)



























































