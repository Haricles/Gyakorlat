'''
A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van az adott listában
(amely a 'Próbáld ki!' gombra kattintva elérhető)! A képernyőre írja is ki a feltételnek megfelelő szavakat!

'''

szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']

osszeg = 0
for elem in szavak:
    if elem[0] == "a" or elem[0] == "A":
        osszeg = osszeg + 1
        print ("A feltételnek megfelelő szavak:",elem)
print ("Összesen ennyi ilyen szó van: ",osszeg)













