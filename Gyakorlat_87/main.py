'''
Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!


'''

lista = []
bemenet = None
while bemenet != "x" and bemenet != "X":
    bemenet = (input("Kerem egy szamot: "))
    if bemenet != "x" and bemenet != "X":
        lista.append(int(bemenet))

print("A lista elemei:",lista)
print ("Legkisebb érték a listában:",min(lista))
print ("Legnagyobb érték a listában:",max(lista))














