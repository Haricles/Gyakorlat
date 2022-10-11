'''
Tökéletesítse az előző gyakorlat scriptjét egy szótár alkalmazásával úgy, hogy a programvégrehajtást a
főmenüből irányítja. A program például a következőt írja ki :
Válasszon:
(V)isszatölt egy már létező fileba mentett szótárat
(B)eszúr adatokat az aktuális szótárba
(Á)tnézi az aktuális szótárat
(M)enti az aktuális szótárat egy fileba
(B)efejezés :
A felhasználó   választásának   megfelelően   tehát   a   megfelelő   függvényt   egy   függvényszótárból
kiválasztva fogjuk hívni.
'''

def szotar_feltoltes(x):
    a=None
    while a != "":
        szotar = {}
        szotar["Nev"]=input("Kerem a nevet: ")
        szotar["Adat"]=(int(input("Kerem a korod: ")),float(input("Kerem a magassagod: ")))
        x.append(szotar)
        a=input("Szeretnél még hozzá adni adatot?")
    return x

def szotar_atnezes(x):
    nev=input("Kerem a nevet: ")
    for elem in x:
        if elem["Nev"]==nev:
            kor=elem["Adat"][0]
            magassag=elem["Adat"][1]
            print (f"Név:{nev} - kor:{kor} éves- magasság: {magassag} m")

def kiiras(x):
    with open("irott.txt","w",encoding="utf-8") as kimenet:
        for elem in x:
            nev=elem["Nev"]
            kor = elem["Adat"][0]
            magassag = elem["Adat"][1]
            kimenet.write(str(nev)+"@"+str(kor)+"#"+str(magassag)+"\n")

def visszaallitas(x):
    with open(x,"r",encoding="utf-8") as bemenet:
        for elem in bemenet:
            szotaram = {}
            sor = elem.strip().split("@")
            szotaram["Nev"]=sor[0]
            valtoztatas=sor[1].split("#")
            tuple_alakitas=(int(valtoztatas[0]),float(valtoztatas[1]))
            szotaram["Adat"]= tuple_alakitas
            print (szotaram)

def main():
    print ("(V)isszatölt egy már létező file-ba mnetett szótárakat")
    print ("(F)eltölti a szótárt.")
    print ("(Á)tnézi az aktuális szótárakat")
    print ("(M)enti az aktuális szótárakat egy file-ba")
    print ("(B)efejezés")
    függvenyszotar={"F":szotar_feltoltes,"Á":szotar_atnezes,"M":kiiras,"V":visszaallitas}
    for key,value in függvenyszotar.items():
        bemenet=input("Kerem adja meg a függvenyt kezdő betűjét: ").upper()
        if bemenet == "F":
            print ((függvenyszotar["F"](lista)))
            break
        elif bemenet == "Á":
            print (függvenyszotar["Á"](lista))
            break
        elif bemenet == "M":
            print (függvenyszotar["M"](lista))
            break
        elif bemenet == "V":
            print (függvenyszotar["V"]("irott.txt"))
            break
        else:
            quit()

lista=[]


main()
#print (szotar_feltoltes(lista))
#szotar_atnezes(lista)
#kiiras(lista)

#visszaallitas("irott.txt")