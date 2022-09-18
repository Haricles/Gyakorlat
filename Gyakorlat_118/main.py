'''
A program generáljon 5 egész számot [0;10] intervallumon, tárolja egy halmazban.
A felhasználónak meg kell próbálni kitalálni ezeket, olyan módon, hogy megad 5 számot,
melyeket szintén halmazban tárol a gép. A program tájékoztassa a felhasználót, a következőkről:
hány darab számot talált el, és melyek ezek; hány számot nem talált el, és melyek ezek; mely számok
kerültek rögzítésre a generálás vagy a felhasználó miatt; mely számok nem szerepeltek egyik halmazban sem!
'''

import random

random_halmaz = set()
while len(random_halmaz) != 5:
        random_szam=random.randint(0,10)
        random_halmaz.add(random_szam)


felhasznalo_halmaza= set()
while len(felhasznalo_halmaza) != 5:
    bement=int(input("Kerek számokat! "))
    felhasznalo_halmaza.add(bement)


metszet= random_halmaz & felhasznalo_halmaza
print ("Ennyi számot talált el a felhasználó!",len(metszet),"\nA számok amiket eltalált:",metszet)

különbseg= random_halmaz-felhasznalo_halmaza
print ("Ennyi számot nem találtál el:",len(különbseg),"\nEzeket a számokat nem találtál el:",különbseg)

print ("A véletlen számokból generált halmaz:",random_halmaz)
print ("A felhasználó által megadott halmaz:",felhasznalo_halmaza)























