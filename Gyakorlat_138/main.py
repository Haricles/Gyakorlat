'''
Készíts egy programot, amely képes tárolni:
- a diákok nevét és osztályát,
- a tanárok nevét és szakját / szakjait,
és ezeket meg is tudja jeleníteni a képernyőn egy összefüggő mondat formájában.

Például:
Szia, a nevem Kiss Péter, és a(z) 10.A osztályba járok.
Szia, a nevem Horváth Zita, biológia-kémia szakos tanár vagyok.
Szia, a nevem Schmidt Emil, matematika szakos tanár vagyok.

Használj objektumorientált megoldást!
- Először gondold végig, milyen osztályokra lesz szükség?
- Van-e lehetőség öröklődés alkalmazása révén optimálisabb kódot írni?
'''

class Szemely():
    def __init__(self,nev):
        self.nev=nev

    def kiiras(self):
        print (f"Szia,a nevem {self.nev}", end="")

class Tanar(Szemely):
    def __init__(self,nev,szak):
        super().__init__(nev)
        self.szak=szak

    def kiiras(self):
        super().kiiras()
        print (f",{self.szak} szakos tanár vagyok.")

class Diak(Szemely):
    def __init__(self,nev,osztaly):
        super().__init__(nev)
        self.osztaly=osztaly

    def kiiras(self):
        super().kiiras()
        print(f" és a(z) {self.osztaly} osztályba járok.")




tanarok=Tanar("Mariann","Matek")
tanarok.kiiras()
diakok=Diak("Mariann","10.B")
diakok.kiiras()

































