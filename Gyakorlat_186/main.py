'''
Mivel Elliot felettesét nagyon lenyűgözte az 1 feladatsorral korábban megírt jelszó-erősség mérő szkript,
ezért egy új feladattal bízza meg alkalmazottját. Elliotnak ki kell válogatnia a vállalat által használt jelszavak
közül azokat, amelyek gyengének minősülnek.

Írj egy gyenge_jelszavak nevű függvényt, amely egy jelszavakat tartalmazó listát kap paraméterül!
A függvény adja vissza ezek közül a gyenge jelszavakat egy listában! Egy jelszót gyengének tekintünk,
ha az alábbi feltételek közül legalább 1 érvényes rá:

A jelszó rövidebb, mint 5 karakter
A jelszó nem tartalmaz számjegy karaktert
A jelszó tartalmazza a jelszo vagy 123 szövegek valamelyikét bármilyen formában
(a kis- és nagybetűket nem megkülönböztetve).

Input: ['Root', 'Kekw2000', 'H0sszuJelszoG0esBrrr', 'Admin123456', 'sub2Pewdiepie', 'asdqwe', 'K1L0']
Return: ['Root', 'H0sszuJelszoG0esBrrr', 'Admin123456', 'asdqwe', 'K1L0']
'''

def gyenge_jelszavak(lista):
    eredmeny=[]
    for jelszo in lista:
        van_szam=False
        for karakter in jelszo:
            if karakter.isdigit():
                van_szam=True

        if len(jelszo)<5 or not van_szam or "jelszo" in jelszo.lower() or "123" in jelszo.lower():
            eredmeny.append(jelszo)
    return eredmeny

jelszavak=['Root', 'Kekw2000', 'H0sszuJelszoG0esBrrr', 'Admin123456', 'sub2Pewdiepie', 'asdqwe', 'K1L0']

print (gyenge_jelszavak(jelszavak))