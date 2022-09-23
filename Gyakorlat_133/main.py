'''
Készíts egy programot, amelyben van egy Negyzet nevű osztály.
Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!

Módosítsd az előző programot úgy, hogy a metódus ne a kerület- illetve a területértékkel térjen vissza,
hanem maga gondoskodjon ezen értékek kiírásáról egy egész mondatos formában.
'''
class Negyzet():
    def __init__(self,oldal=0,hossz=0):
        self.oldal=oldal
        self.hossz=hossz

    def kerulet(self):
        print (f"A négyzet kerülete: {2*(self.oldal+self.hossz)}")

    def terulet(self):
        print (f"A négyzet területe: {self.oldal*self.hossz}")


osztaly=Negyzet(2,9)
osztaly.kerulet()
osztaly.terulet()

























































