'''
a: Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút).
A program a írja ki a képernyőre az adatszerkezet! A felhasználónak legyen lehetősége ezt az
adatszerkezetet egy kulcs-érték párral bővítenie. A program végül írja ki a képernyőre a frissített adatszerkezetet!

b: Módosítsd úgy a programot, hogy a felhasználónak többször is legyen lehetősége bővíteni az adatszerkezetet!
'''

kutya_adatok={"Nev":"Bodri","Kor":10,"Oltás":True}
print (kutya_adatok)
kulcs = None
while kulcs != "":
    kulcs = input("Kerem a kulcsot! ")
    if kulcs != "":
        kutya_adatok[kulcs]=input("Kerem az értéket! ")
        print (kutya_adatok)