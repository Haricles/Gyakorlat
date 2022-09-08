'''
Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt!
A szavakat tárolja el a program egy listában! Az adatbekérés befejezte után írja ki
a program a lista elemeit, a legrövidebb és a leghosszabb szót!

'''

lista = []
bemenet = None
while bemenet != "":
    bemenet = input("Kerem a szavakat: ")
    if bemenet != "":
        lista.append(bemenet)

legkisebb = lista[0]
for elem in lista:
    if len(legkisebb) > len(elem):
        legkisebb = elem

leghosszabb = lista[0]
for elem in lista:
    if len(leghosszabb) < len(elem):
        leghosszabb = elem


print ("A lista elemei:",lista)
print ("A legrövidebb szó: ",legkisebb)
print ("A leghosszabb szó: ",leghosszabb)















