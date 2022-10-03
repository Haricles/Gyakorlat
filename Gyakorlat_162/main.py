'''
Írjon egy függvényt, ami megszámolja, hogy az argumentumként megadott karakter hányszor fordul elő
egy adott mondatban.
'''

def szamolas(mondat,karakter):
    i=0
    for elem in mondat:
        if elem == karakter:
            i+=1
    print (i)


szamolas("Volt egyszer egy vadneyugat.","t")







