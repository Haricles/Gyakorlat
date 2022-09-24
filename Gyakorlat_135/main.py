'''
Készíts egy programot, amely objektumorientált módon tartja nyilván kutyák adatait (név, életkor, nem)!
A nevét a felhasználó adja meg, az életkorát és a nemét véletlenszerűen határozza meg a program!
Befejezésként a program a képernyőre írja ki a megadott kutyák adatait!

'''
import random

class Kutya_adatok():
    nem=["him","szuka"]
    
    def __init__(self,nev=None,eletkor=random.randint(0,30),nem=random.choice(nem)):
        self.nev=nev
        self.eletkor=eletkor
        self.nem=nem


kutya=Kutya_adatok("Cuki")
print (kutya.nem)
print(kutya.eletkor)
print (kutya.nev)






























































