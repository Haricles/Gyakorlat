'''
Készíts egy listát amely 8 diák adatait tartalmazza. A lista elemei szótárak legyenek,
egy-egy szótár egy-egy diák adatait tárolja. A szótárban lévő kulcsok és a hozzájuk tartozó értékek:
"név": a vezeteknevek és a keresztnevek nevű listából véletlenszerűen választott és párosított elemek
"életkor": véletlenszám [14;19] intervallumban
"évfolyam": véletlenszám [9;12] intervallumban
"osztály": A, B, C vagy D lehet
"cím": beágyazott szótár melynek kulcsai:
"település": telepulesek nevű listából véletlenszerűen választva
"utca": utcak nevű listából véletlenszerűen választva
"házszám": véletlenszám [1;50] intervallumban
A program pprint modul pprint() függvénye segítségével áttekinthető módon jelenítse meg a diákok adatait a képernyőn!
Tipp: listából véletlenszerűen választani a random modul choice() függvényével tudunk a legegyszerűbben.
'''
import random
import pprint

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna"]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér"]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]

vez_kereszt= random.choice(vezeteknevek)+" "+random.choice(keresztnevek)
évfoly=random.randint(9,12)
osztaly = ["A","B","C","D"]
települes=random.choice(telepulesek)+" "+ random.choice(utcak)+" utca "+ str(random.randint(1,50))

diak_adatok=[{"Név":vez_kereszt,"Kor":random.randint(14,19),
              "Évfolyam":évfoly,
              "Osztaly":random.choice(osztaly),
              "Cím":települes}]

print (pprint.pformat(diak_adatok))
