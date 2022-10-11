'''
Definiáljon egy Domino() osztályt, amivel a dominójáték köveit szimuláló objektumok hozhatók létre.
Az osztály constructora inicializálja a dominó A és B felén lévő pontok értékeit (az alapértelmezett
értékek =0).
Definiáljon két másik metódust :
a kiir_pontok() metódust, ami kiírja a két oldalon levő pontokat
az ertek() metódust, ami a két oldalon lévő pontok összegét adja meg.
Példák az osztály alkalmazására :
d1 = Domino(2,6)
 d2 = Domino(4,3)
d1.kiir_pontok()
 A oldal : 2  B oldal : 6
d2.kiir_pontok ()
 A oldal : 4  B oldal : 3
print "Összes pont :", d1.ertek() + d2.ertek ()
 15
lista_dominok = []
for i in range(7):
 lista_dominok.append(Domino(6, i))
 print lista_dominok

 stb., stb.
'''

class Domino():
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b

    def kiir_pontok(self):
        print (f"A oldal: {self.a} B oldal: {self.b}")

    def ertek(self):
        print ("A két oldal összege:",self.a+self.b)

d1 = Domino(2,6)
d2 = Domino(4,3)
d1.kiir_pontok()
d2.kiir_pontok()
d1.ertek()
d2.ertek()

lista_dominok=[]
for i in range(7):
    lista_dominok.append(Domino(6, i))
print (lista_dominok)

