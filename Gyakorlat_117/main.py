'''
A mellékelt ZIP állományban találsz egy forrásfájlt (autok_lista.txt), amely tartalmazza egy autószerelő műhelyben
lévő autók adatait. Az adatok sorrendben a következők:
rendszám, márka, típus, életkor, 0 = még nincs megjavítva 1 = megjavított, javítás költsége.

A muhely.py nevű fájlban lévő program pedig beolvassa ezeket az adatokat és eltárolja egy szótárakat tartalmazó listában.

Folytatsd a muhely.py programot az alábbiak szerint!
1. A program írja ki a képernyőre a legöregebb autó rendszámát, márkáját, típusát és korát! (Csak egy ilyen van!)
    ------------- 1. feladat -------------
    A legöregebb autó: JTZ-774, Ford Fiesta, 25 éves.

2. A program írja ki a képernyőre a már megjavított autók rendszámát!
    ------------- 2. feladat -------------
    A már megjavított autók rendszáma:
    TRU-234
    OPO-223
    ETW-231
    SSA-772
    GGT-434

3. A program számolja ki, és írja ki a képernyőre az egy autóra eső átlagos szervízköltséget!
    ------------- 3. feladat -------------
    Az egy autóra jutó átlagos javítási költség: 55425 Ft.

4. A program kérjen be egy rendszámot, vizsgálja meg és tájékoztassa a felhasználót, hogy az
adott rendszámú autó a műhelyben van-e.
    ------------- 4. feladat -------------
    Adjon meg egy rendszámot (pl. ABC-123)!  SSA-772
    A megadott rendszámú autó a műhelyben van.

5. A program kérjen be egy betűt, vizsgálja meg és tájékoztassa a felhasználót, hogy van-e a műhelyben olyan autó,
amelynek a márkája vagy a típusa tartalmazza az adott betűt! A kis- és nagybetűket ne különböztesse meg a program!
    ------------- 5. feladat -------------
    Adjon meg egy betűt!    X
    A megadott betű az alábbi autók márka- vagy típusmegnevezésében fordul elő:
    Ford C-Max
'''


'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())

'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''

auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

print (autok)
#1.feladat
max_kor= autok[0]['kor']
for kocsi in autok:
    if kocsi['kor'] > max_kor:
        max_kor = kocsi['kor']
print ("A legidősebb autó:",kocsi['rendszam'],kocsi['marka'],kocsi['tipus'],max_kor,"éves.")

for szam in autok:
    if szam['javitva'] == True:
        print ("A már megjavított autók rendszáma:",szam['rendszam'])
#1.feladat vége
#2.feladat
osszeg = 0
for elem in autok:
    if elem['koltseg']:
        osszeg = osszeg + (elem['koltseg'])
atlag = osszeg // len(autok)
print ("Az egy autóra jutó átlagos javítási költség:",atlag,"Ft")
#2.feladat vége
#3.feladat
a = input("Kerem a rendszámot: ").upper()
for elem in autok:
    if elem['rendszam'] == a:
        print ("A megadott rendszámú autó a műhelyben van.")
#3.feladat vége
#4.feladat
i = 0
while i < len(autok):
    if autok[i]['rendszam']==a:
        break
    else:
        i+=1
if i < len(autok):
    print ("Benne van")
else:
    print ("Nincs benne")
#4.feladat vége
#5.feladat
betü = input("Kerek egy betüt! ")
i = 0
while i < len(autok):
    if autok[i]['marka'].__contains__(betü) or autok[i]['tipus'].__contains__(betü):
        break
    else:
        i+=1
if i < len(autok):
    print ("Tartalmazza a betüt",autok[i])
else:
    print ("Nem tartalmazza a betüt")
#5.feladat vége










































