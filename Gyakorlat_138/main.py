'''
Fejleszd tovább az előző programot úgy, hogy az hozzon létre öt Diak-objektumot.
A nevet egy-egy vezeték és keresztneveket tartalmazó listából állítsa össze véletlenszerűen,
az osztályt és a születési évet pedig szintén véletlenszerűen generálja! A Diak-objektumokat egy listában tárolja!
A program a listát bejárva írja ki a diákadatokat a képernyőre!
'''
import datetime
import random


class Diak():
    diak_lakcim="Budapest"
    vezeteknev= ["Toth","Balogh","Nagy","Kiss","Varga"]
    keresztnev= ["Virag","Károly","Béla","Gergő","Gizi"]
    osztalyok=["A","B","C","D"]

    def __init__(self,nev=None,osztaly=None,szulev=0):
        self.nev=nev
        self.osztaly=osztaly
        self.szulev=szulev

    def nev_valaszto(self):
        return random.choice(type(self).vezeteknev) +" "+ random.choice(type(self).keresztnev)

    def osztaly_valaszto(self):
        return str(random.randint(9,12))+ "."+ random.choice(type(self).osztalyok)

    def diak_eletkor(self):
        return datetime.datetime.now().year-self.szulev

    def kiiratas(self):
        print (f"Szia, {self.nev} vagyok, a {self.osztaly} osztályba járok, {self.diak_eletkor()} éves vagyok.")

    @staticmethod
    def iskola():
        print ("Harjá x,y iskola!")
    @classmethod
    def lakcimkiiras(cls):
        print (cls.diak_lakcim)

diakok=Diak("Kiss Péter","10.A",2006)
print (diakok.nev)
print(diakok.osztaly)
print(diakok.szulev)
print(diakok.diak_eletkor())
diakok.kiiratas()

diakok.iskola()
diakok.lakcimkiiras()

diakok_01=Diak()
diakok_02=Diak()
diakok_03=Diak()
diakok_04=Diak()
diakok_05=Diak()

print (diakok.nev_valaszto())
print (diakok.osztaly_valaszto())



















































