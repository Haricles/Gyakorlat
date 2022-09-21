'''
A mellékelt fájl Rainer Maria Rilke: A párduc című versét tartalmazza Szabó Lőrinc fordításában
(forrás: Magyar Elektronikus Könyvtár). Az általad írt program olvassa be a fájl tartalmát a read() metódussal,
és adja meg a válaszokat az alábbi kérdésekre:
- hány betűt tartalmaz a vers,
- hány magánhangzót tartalmaz a vers,
- hány szó fordul elő a versben?
'''

abc= ["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
szöveghossz=0
maghang=0
szavakszama=0
with open("Rilke_A_parduc.txt","r",encoding="utf-8") as file:
    olvasas=file.read()
    olvasas_finomitasa=olvasas.split()
    for elem in olvasas_finomitasa:
        szavakszama +=1
    for elem in olvasas:
        szöveghossz +=1
        if elem in abc:
            maghang+=1

print ("A szöveg hosszúsága:",szöveghossz,"\nEnnyi db magánhangzót tartalmaz a szöveg:",maghang,
       "\nEnnyi szó fordul elő a szövegben",szavakszama)
































