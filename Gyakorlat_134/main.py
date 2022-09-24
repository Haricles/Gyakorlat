'''
Az 1.1 feladatban meghatározottak szerint készíts egy programot, amely a felhasználótól egymás után
bekér négyzetek oldalhosszát egészen addíg, amíg a felhasználó 0 értéket nem ad meg!
Ezen adat alapján a program hozzon létre negyzet objektumokat, melyeket egy listában tárol!
A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
'''

class Negyzet():
    def __init__(self,oldal=1,hossz=1):
        self.oldal=oldal
        self.hossz=hossz

    def kerulet(self):
        print (f"A négyzet kerülete: {2*(self.oldal+self.hossz)}")

    def terulet(self):
        print (f"A négyzet területe: {self.oldal*self.hossz}")

lista=[]
negyzet=Negyzet(1,1)
while (negyzet.oldal != 0) and (negyzet.hossz != 0):
    negyzet = Negyzet(int(input("Kerem az oldalt:")), int(input("Kerem a hosszt!")))
    if (negyzet.oldal != 0) and (negyzet.hossz != 0):
        lista.append(negyzet)

for elem in lista:
    (elem.terulet(),elem.kerulet())


































































