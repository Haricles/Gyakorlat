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

Fejezze be a 10.45 gyakorlatot (mini adatbázis rendszer) két függvény hozzáadásával : az egyik a szótár
file-ba történő kiírására, a másik a szótárnak a megfelelő file-ból történő visszaállítására szolgáljon.
A file minden sora egy szótárelemből álljon. Legyenek jól elkülönítve az adatok :
- a kulcs és az érték (vagyis a személynév egyrészről és az « életkor +testmagasság » másrészről.)
- az « életkor +testmagasság » csoportban két numerikus adat van.
Két különböző elválasztó karaktert használjon, például « @ »-ot a kulcs és az érték, illetve a « # »-ot az
értéket alkotó adatok elválasztására  :
Juliette@18#1.67
Jean-Pierre@17#1.78
Delphine@19#1.71
Anne-Marie@17#1.63
stb.
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

def visszaallitas():
    with open("irott.txt","r",encoding="utf-8") as bemenet:
        for elem in bemenet:
            szotaram = {}
            sor = elem.strip().split("@")
            szotaram["Nev"]=sor[0]
            valtoztatas=sor[1].split("#")
            tuple_alakitas=(int(valtoztatas[0]),float(valtoztatas[1]))
            szotaram["Adat"]= tuple_alakitas
            print (szotaram)

lista=[]

print (szotar_feltoltes(lista))
szotar_atnezes(lista)
kiiras(lista)

visszaallitas()