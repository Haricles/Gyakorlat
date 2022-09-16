'''
Írj egy programot, amely egy ötbetűs főneveket tartalamzó listából véletelenszerűen választ egyet,
amit a játékosnak egy-egy betű megadásával kell kitalálnia! A főprogramot a main() függvény tartalmazza,
és ezen kívűl legyen még minimum 2 - részfeladatokat megvalósító - függvény! A program az alábbiak szerint műdködjön:

    Találd ki, melyik ötbetűs főnévre gondoltam!
    Adj meg egy betűt! a
    Találat!
    Jelenlegi állás: ____a
    Rossz tippek:
    ------------------------------------------
    Adj meg egy betűt! é
    Sajnos nem talált!
    Jelenlegi állás: ____a
    Rossz tippek: é
    ------------------------------------------
    Adj meg egy betűt! b
    Találat!
    Jelenlegi állás: __b_a
    Rossz tippek: é
    ------------------------------------------

'''
import random

def szovalaszto():
    szotar=["kalap","tégla","lámpa","tábla","kocsi"]
    return random.choice(szotar)

def nem_megoldott(jatekos):
    return "_" in jatekos

def tipp_bekero():
    return input("Adj meg egy betüt!")

def ertekel(gep,karakter,jatekos,nem_jo):
    talalat=False
    for index,betu in enumerate(gep):
        if karakter == betu:
            jatekos[index] =karakter
            talalat = True
    if talalat:
        print ("Találat!")
    else:
        print ("Sajnos nem talált!")
        nem_jo.append(karakter)
    print (f'Jelenlegi állás: {"".join(jatekos)}')
    print (f'Rossz tippek: {",".join(nem_jo)}')
    print ("----------------------------------\n")

def main():
    print ("Találd ki,melyik ötbetűs főnévre gondoltam! ")
    kitalálandó = szovalaszto()
    allas = ["_","_","_","_","_"]
    rossz_tippek= []
    probalkozasok = 0
    while nem_megoldott(allas):
        probalkozasok +=1
        tipp = tipp_bekero()
        ertekel(kitalálandó,tipp,allas,rossz_tippek)
    print(f"Gratulálok! Kitaláltad {probalkozasok} próbálkozásból.")

main()

