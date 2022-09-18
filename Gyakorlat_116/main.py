'''
Írj egy programot, amelyben könyvek adatait (szerző, cím) tudja rögzíteni a felhasználó.
A könyvek adatainak tárolására használjon a program szótárakat, amelyek egy lista elemei legyenek!
Az adatbekérés addig folytatódjon, amíg a felhasználó a szerző megadásakor nem gépel be adatot, csupán ENTER-t üt!
A program ekkor listázza ki a már bevitt adatokat, és fejezze be a működését!
'''

könyv_adatok = []
könyv_szotar = {"Szerző":None}
while könyv_szotar["Szerző"] != "":
    könyv_szotar = {"Szerző": input("Kerem a szerzőt! "), "Cím": input("Kérem a címet: ")}
    if könyv_szotar["Szerző"] != "":
        könyv_adatok.append(könyv_szotar)

print (könyv_adatok)