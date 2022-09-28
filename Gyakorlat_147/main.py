'''
Próbálja  megírni a  megtalal()  függvényt, ami az ellenkezőjét csinálja, mint amit az indexoperátor
(vagyis a []) tesz. Ahelyett, hogy egy megadott indexhez megtalálja az annak megfelelő karaktert, ennek
a függvénynek egy adott karakterhez tartozó indexet kell megtalálni.
Máshogyan   fogalmazva,   egy   olyan   függvényt   kell   írni,   ami   két   argumentumot   vár :   a   kezelendő
karakterlánc nevét és a keresendő karaktert. A függvénynek visszatérési értékként az első ilyen karakter
stringbeli indexét kell megadni a karakterláncban. Így például : print megtalal("Juliette &
Roméo", "&") eredménye :  9

Figyelem   :   Gondolni   kell   minden   lehetséges   esetre.   Arra   is   számítanunk   kell,   hogy   a   függvény
visszatérési   értékként   egy   speciális   értéket   (például  -1-et)   ad,   ha   a   keresett   karakter   nincs   a
karakterláncban.
'''

karakter= "valamivanalevegőbenésnemtudomhogymi."

def megtalal(sztring,megtalalando):
    if megtalalando in sztring:
        return sztring.index(megtalalando)
    else:
        return -1

print (megtalal(karakter,"x"))






































