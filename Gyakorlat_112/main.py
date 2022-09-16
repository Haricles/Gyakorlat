'''
Írj egy programot, amely szótárban tárolja egy macska nevét, korát.
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot.
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg, mire módosítsa,
végül írja ki a képernyőre a frissített adatszerkezetet!


'''
macska_adatok={"Nev":"Kandúr","Kor":5}

kulcs_modositas= input("Melyik adatot módosítsam? ")
print (macska_adatok[kulcs_modositas])
ertek_mosoitas= input("Mire módosítsam? ")
macska_adatok[kulcs_modositas]= ertek_mosoitas
print (macska_adatok[kulcs_modositas])


