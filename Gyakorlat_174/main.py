'''
Írjon egy scriptet, ami egy szótárral működő mini-adatbázist hoz létre, melyben a barátainak a nevét,
életkorát, testmagasságát tárolja. A scriptnek két függvényt kell tartalmazni: az első a szótár
feltöltésére, a második az átnézésére szolgál.A feltöltő függvényben alkalmazzon egy programhurkot a
felhasználó által beírt adatok elfogadására.
A tanulók neve lesz a kulcs és az értékek tuple-kből fognak állni (életkor, testmagasság). Az életkor
években (egész típusú adat), a testmagasság méterben (real típusú adat) lesz kifejezve.
Az átnézésre szolgáló függvény is tartalmaz egy programhurkot. Ebben a felhasználó valamilyen nevet
ad   meg,   hogy   visszatérési   értékként   megkapja   a   megfelelő életkor-testmagasság   párt.   A   kérés
eredményének egy formázott szövegsornak kell lenni, mint például : « Név : Jean Dhoute - kor : 15 éves
- magasság : 1.74 m ».

'''



def szotar_feltoltes(x):
    a=None
    while a != "":
        szotar={}
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

lista=[]

print (szotar_feltoltes(lista))
szotar_atnezes(lista)