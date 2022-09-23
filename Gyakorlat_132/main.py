'''
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!
'''
class Negyzet():
    def __init__(self,oldal=0,hossz=0):
        self.oldal=oldal
        self.hossz=hossz

    def kerulet(self):
        return 2*(self.oldal+self.hossz)

    def terulet(self):
        return self.oldal*self.hossz


osztaly=Negyzet(2,6)
print (osztaly.kerulet())
print (osztaly.terulet())

























































