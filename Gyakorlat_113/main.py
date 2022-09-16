'''
Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút).
A program a írja ki a képernyőre az adatszerkezet! A felhasználónak legyen lehetősége ezt az
adatszerkezetet egy kulcs-érték párral bővítenie. A program végül írja ki a képernyőre a frissített adatszerkezetet!
'''

kutya_adatok={"Nev":"Bodri","Kor":10,"Oltás":True}
print (kutya_adatok)
kutya_adatok[input("Kerem a kulcsot! ")]=input("Kerem az értéket! ")
print (kutya_adatok)