'''
A feladat linkje: https://cservz.github.io/teaching/szkriptnyelvek/feladatsorok/05/
'''

def beolvas():
    lista = []
    with open("playlist.csv", "r", encoding="utf-8") as file:
        for adat in file:
            adatok = adat.strip()
            adatok = adatok.split(";")
            dict_adatok = {"eloado": adatok[0], "cim": adatok[1], "mufaj": adatok[2], "hossz": int(adatok[3])}
            lista.append(dict_adatok)
    return lista

def teljes_hossz(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem["hossz"]
    perc = osszeg // 60
    masodperc = osszeg % 60
    return f"A lejatszasi lista hossza: {perc} perc, {masodperc} masodperc"

def leghosszabb_rockzene(lista):
    rock_lista = []
    for elem in lista:
        if elem["mufaj"] == "rock":
            rock_lista.append(elem["hossz"])
    legnagyobb = rock_lista[0]
    for elem in rock_lista:
        if legnagyobb < elem:
            legnagyobb = elem
    for elem in lista:
        if legnagyobb == elem["hossz"]:
            cim = elem["cim"]
    with open("03_leghosszabb_rock.txt", "w", encoding="utf-8") as kimenet:
        kimenet.write(cim)

def leggyakoribb_mufaj(lista):
    szotar = {}
    for elem in lista:
        mufaj = elem["mufaj"].upper()
        if mufaj not in szotar:
            szotar[mufaj] = 1
        else:
            szotar[mufaj] += 1
    max_elofordulas = 0
    leggyakoribb = ""
    for key, value in szotar.items():
        if value > max_elofordulas:
            max_elofordulas = value
            leggyakoribb = key
    with open("04_kedvenc_mufaj.txt", "w", encoding="utf-8") as kimenet:
        kimenet.write(leggyakoribb)

def zeneket_csoportosit(lista):
    uj_szotar = {}
    for elem in lista:
        eloado = elem["eloado"]
        hossz = elem["hossz"]
        if eloado not in uj_szotar:
            uj_szotar[eloado] = hossz
        else:
            uj_szotar[eloado] += hossz
    with open("05_osszegzes.txt", "w", encoding="utf-8") as kimenet:
        for key, value in (sorted(uj_szotar.items())):
            szoveg = f"{key} - osszesen {value} masodpercnyi zene"
            kimenet.write("\n" + szoveg)

def zeneket_listaz(lista, nev):
    nev = nev.replace(" ", "_").lower()
    uj_lista = []
    nev = nev.replace("_", " ").lower()
    for elem in lista:
        if elem["eloado"].lower() == nev:
            uj_lista.append(elem)
    with open(nev, "w", encoding="utf-8") as kimenet:
        if len(uj_lista) == 0:
            kimenet.write("Nincs ilyen eloado a lejatszasi listaban!")
        else:
            for elem in uj_lista:
                kimenet.write(f"{elem['cim']};{elem['mufaj']};{elem['hossz']}\n")

def zeneket_torol(lista, eloadok_lista):
    with open("07_torolt.txt", "w", encoding="utf-8") as kimenet:
        for elem in lista:
            if elem["eloado"] not in eloadok_lista:
                kimenet.write(f"{elem['eloado']};{elem['cim']};{elem['mufaj']};{elem['hossz']}\n")

if __name__ == '__main__':
    lejatszasi_lista = beolvas()
    zeneket_torol(lejatszasi_lista, ["Imagine Dragons", "Rick Astley", "Powerwolf"])
    zeneket_listaz(lejatszasi_lista, "POWERWOLF")
    leghosszabb_rockzene(lejatszasi_lista)
    leggyakoribb_mufaj(lejatszasi_lista)
    zeneket_csoportosit(lejatszasi_lista)