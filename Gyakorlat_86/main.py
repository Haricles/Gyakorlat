'''
Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt!
A számokat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!


'''

lista = []
bemenet = None
while bemenet != "":
    bemenet = (input("Kerem egy szamot: "))
    if bemenet != "":
        lista.append(int(bemenet))

print("A lista elemei:",lista)
print ("Legkisebb érték a listában:",min(lista))
print ("Legnagyobb érték a listában:",max(lista))














