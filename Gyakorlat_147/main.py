'''
Próbálja  megírni a  megtalal()  függvényt, ami az ellenkezőjét csinálja, mint amit az indexoperátor
(vagyis a []) tesz. Ahelyett, hogy egy megadott indexhez megtalálja az annak megfelelő karaktert, ennek
a függvénynek egy adott karakterhez tartozó indexet kell megtalálni.
Máshogyan   fogalmazva,   egy   olyan   függvényt   kell   írni,   ami   két   argumentumot   vár :   a   kezelendő
karakterlánc nevét és a keresendő karaktert. A függvénynek visszatérési értékként az első ilyen karakter
stringbeli indexét kell megadni a karakterláncban. Így például : print megtalal("Juliette &
Roméo", "&") eredménye :  9

'''

karakter= "valamivanalevegőbenésnemtudomhogymi."

def megtalal(sztring,megtalalando):
    return sztring.index(megtalalando)

print (megtalal(karakter,"ő"))






































