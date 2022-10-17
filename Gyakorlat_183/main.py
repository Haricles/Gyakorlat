'''
Balázs a zsebpénzéből egy új mikrofont szeretne venni. Szerencséjére a kedvenc webshopja épp kiárusítást tart,
így minden szórakoztató elektronikai termék akciósan vásárolható meg.

Írj egy akcios_ar nevű függvényt, amely két paramétert vár: a webshopban található mikrofonok eredeti árát
(egész számokat tároló lista) és a leárazás mértékét százalékban (valós szám)!
A függvény csökkentse a listában lévő árakat az adott százalékkal, és térjen vissza az így kapott listával!
Az árak továbbra is egészek legyenek (ne tizedestörtek)!

Input: [5000, 12000, 10000, 29000, 47000], 30.0
Return: [3500, 8400, 7000, 20300, 32900]
'''

def akcios_ar(ar,akcio):
    akcios_ar=[]
    for elem in ar:
        kedvezmenyes_ar=elem-elem*(akcio/100)
        akcios_ar.append(int(kedvezmenyes_ar))
    return akcios_ar

eredeti_ar=[5000, 12000, 10000, 29000, 47000]

print (akcios_ar(eredeti_ar,30))