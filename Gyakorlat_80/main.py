'''
Fejlesszük tovább a 2.2 programot úgy, hogy a felhasználónak többször is legyen lehetősége újabb tippet megadnia.
A bekérés addig folytatódjon, amíg a felhasználó nem ad meg betűt, csupán egy ENTER-t üt!

Igyekezz minél felhasználóbarátabbá tenni a programot! A programnak lehetnek egyéb hasznos funkciói, például gyűjtheti
 és kiírhatja a jó és a rossz tippeket (betűket).
'''

a = "karalábé"
bemenet = None
tipp_jo = ""
tipp_rossz = ""

while bemenet != "":
    bemenet = input("Kerek egy betüt: ")
    if bemenet != "":
        if bemenet in a:
            tipp_jo = bemenet + tipp_jo
            print ("Benne van!","A tárolt szó:",a)

        else:
            tipp_rossz = bemenet + tipp_rossz
            print ("Nincs benne!","A tárolt szó:",a)


print ("Eltalált betűk:",tipp_jo,"Elvétett betűk:",tipp_rossz)










