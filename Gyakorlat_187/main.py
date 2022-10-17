'''
Írj egy egyedi_szavak_szama nevű függvényt, amely egy szöveget kap paraméterül
(a szöveg szóközzel elválasztott szavakat tartalmaz)! A függvény adja vissza,
hogy hány különböző szó található a szövegben!

A kis- és nagybetűket ne különböztesd meg (tehát pl. alma és ALMA ugyanaz a szó)!
A szavak végén lévő pontoktól, felkiáltójelektől, kérdőjelektől és vesszőktől szabadulj meg
(tehát például Alma? és alma ugyanaz a szó)! Feltehetjük, hogy ezek az
írásjelek csak szavak végén fordulnak elő a szövegben.

Input: 'A macska, vagy mas neven a hazi macska  kisebb termetu husevo emlos, amely a macskafelek csaladjaba tartozik.'
Return: 14
'''

def egyedi_szavak_szama(sztring):
    uj_sztring=""
    for betu in sztring:
        if betu == "," or betu== "?" or betu=="!" or betu==".":
            pass
        else:
            uj_sztring+=betu
    print (uj_sztring)

    uj_szavak=[]
    szavak_lista=uj_sztring.split()
    for elem in szavak_lista:
        szo=elem.lower()
        if szo not in uj_szavak:
            uj_szavak.append(szo)
    return len(uj_szavak)

mondat="A macska, vagy mas neven a hazi macska kisebb  termetu husevo emlos, amely a macskafelek csaladjaba tartozik."
print (egyedi_szavak_szama(mondat))