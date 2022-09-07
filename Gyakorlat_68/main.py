'''
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín kerüljön
 felvételre a listába, és csak ezután történjen meg a lista tartalmának kiírása!
'''

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']
bemenet = input("Kerek egy színt! ")
if bemenet in paletta:
    print ("Már szerepel benne! ","Eddig ennyiszer szerepel a listában: ",paletta.count(bemenet))
else:
    print ("Még nincs benne!")



print ("A lista szinei: ")
for elem in paletta:
    if bemenet not in paletta:
        paletta.append(bemenet)
    print (elem,"",end=",")




