'''
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám!
Kezeld azt az esetet is, ha a két szám egyenlő!


'''


def osszahasonlitas(a,b):
    if a < b:
        print (f" {b} nagyobb mint {a}!")
    elif a > b:
        print (f" {a} nagyobb mint a {b}!")
    else:
        print (f" {a} és {b} egyenlő!")

osszahasonlitas(9,9)












