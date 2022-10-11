'''
 Definiáljon   egy  BankSzamla()  osztályt,   ami   lehetővé   teszi   a  szamla1,  szamla2,   stb.   objektumok
létrehozását.   Az   osztály   constructora   két   példányattribútumot   inicializáljon :   a   nev   és   egyenleg
attribútumokat a 'Dupont' és 1000 alapértelmezett értékekkel.
Definiáljon három másik metódust is :
- betesz(osszeg) adott összeget tesz a számlára
- kivesz(osszeg) adott összeget vesz le a számláról
- kiir() kiírja a számlatulajdonos nevét és a számlája egyenlegét.
Pédák az osztály alkalmazására :
szamla1 = BankSzamla('Duchmol', 800)
szamla1.betesz(350)
szamla1.kivesz(200)
szamla1.kiir()
Duchmol bankszálaegyenlege 950 euro.
szamla2 = BankSzamla()
szamla2.betesz (25)
szamla2.kiir()
Dupont bankszálaegyenlege 1025 euro.

'''

class BankSzamla():
    def __init__(self,nev="Dupont",egyenleg=1000):
        self.nev=nev
        self.egyenleg=egyenleg

    def betesz(self,összeg):
        self.egyenleg=self.egyenleg+összeg

    def kivesz(self,összeg):
        self.egyenleg=self.egyenleg-összeg

    def kiir(self):
        print (f"{self.nev} bankszámla egyenlege: {self.egyenleg} euro")


szamla_1=BankSzamla("Duchmo",800)
szamla_1.betesz(350)
szamla_1.kivesz(200)
szamla_1.kiir()

szamla_2=BankSzamla()
szamla_2.betesz(25)
szamla_2.kiir()

