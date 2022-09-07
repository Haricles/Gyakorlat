'''
Alakítsuk át az előbbi programot úgy, hogy a program arról adjon tájékoztatást, hogy pontosan hányszor szerepel a
felhasználó által megadott szín a listában!
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




