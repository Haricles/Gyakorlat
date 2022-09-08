'''
A program számolja össze, hogy hány darab 'E' vagy 'e' betűt tartalmazó szó van az adott listában
A képernyőre írja is ki a feltételnek megfelelő szavakat!

'''

szavak = ['Elemér', 'Emma', 'ajtó', 'róka', 'egér']
osszeg = 0
for elem in szavak:
    if "e" in elem or "E" in elem:
        osszeg = osszeg + 1
        print (elem)
print ("'e' és 'E' betűt tartalmazó szavak száma:",osszeg)















