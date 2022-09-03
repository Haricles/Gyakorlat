'''
Definiáljon egy szavakSzama(mon) függvényt,ami a mon mondatban található szavak számát adja vissa.
(Szavaknak olyan karaktercsoportokat tekintünk, amik között szóköz van.
'''

def szavakSzama(mon):
    a = mon.split()
    return len(a)

print (szavakSzama("Programozó leszek és addig csinálom még el nem érem a célom!"))

