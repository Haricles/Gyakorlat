'''
Hozz létre egy Diak nevű osztályt. Attribútumai: név, osztály, születési év.
Az egyik metódusa állíptsa meg az aktuális év és a születési év alapján a diák életkorát, a másik metódusa
pedig adjon vissza egy f-sztringet, amelyben mondatszerűen szerepelnek a
diák adatai: Szia, Kiss Péter vagyok, a 10.A osztályba járok, 16 éves vagyok.
'''
class Diak():
    def __init__(self,nev=None,osztaly=None,szulev=0):
        self.nev=nev
        self.osztaly=osztaly
        self.szulev=szulev

    def diak_eletkor(self):
        return 2022-self.szulev

    def kiiratas(self):
        print (f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.diak_eletkor()} éves vagyok.")

diakok=Diak("Kiss Péter","10.A",2006)
print (diakok.nev)
print(diakok.osztaly)
print(diakok.szulev)
print(diakok.diak_eletkor())
diakok.kiiratas()

























































