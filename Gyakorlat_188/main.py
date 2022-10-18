'''
Írj egy felvaltva nevű függvényt, amely egy több szóból álló szöveget vár paraméterben!
A függvény alakítsa át a szöveget úgy, hogy az egymás utáni szavak felváltva legyenek csupa nagybetűsek,
illetve csupa kisbetűsek (lásd: első példa)! A szöveg első szava mindig csupa nagybetűs.
A visszatérési érték az átalakított szöveg.

Kezeld le azt az esetet, amikor a függvény egy 2-nél kevesebb szóból álló szöveget kap paraméterül!
Ekkor a visszatérési érték a HIBA! szöveg legyen!

Input: 'Tajekoztatjuk utasainkat, hogy a Szeged felol erkezo szemelyvonat varhatoan otven percet kesik.'
Return: 'TAJEKOZTATJUK utasainkat, HOGY a SZEGED felol ERKEZO szemelyvonat VARHATOAN otven PERCET kesik.'

Input: 'Sajt'
Return: 'HIBA!'
'''

mondat = "Tajekoztatjuk utasainkat, hogy a Szeged felol erkezo szemelyvonat varhatoan otven percet kesik."
uj_sztring=""
lista_mondat=mondat.split()
for elem in range(len(lista_mondat)):
    if elem % 2 == 0:
        uj_sztring+=lista_mondat[elem].upper()+" "
    else:
        uj_sztring+=lista_mondat[elem].lower()+" "

print (uj_sztring)
