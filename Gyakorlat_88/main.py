'''
Alakítsd át úgy az előbbi programot, hogy a legkisebb és legnagyobb páros számot határozza meg!

'''

lista = []
bemenet = None
while bemenet != "x" and bemenet != "X":
    bemenet = (input("Kerem egy szamot: "))
    if bemenet != "x" and bemenet != "X":
        lista.append(int(bemenet))

print("A lista elemei:",lista)
print ("Legkisebb páros szám a listában:",min([elem for elem in lista if elem % 2==0]))
print ("Legnagyobb páros a listában:",max([elem for elem in lista if elem % 2==0]))














