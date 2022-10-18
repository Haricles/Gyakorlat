'''
A kedvenc gyorséttermünkben a vásárlók belépés után sorszámot húznak, amely alapján leadhatják a rendelésüket.
Az étteremben két kassza üzemel: egyiknél a páros, másiknál pedig a páratlan sorszámú rendeléseket szolgálják ki.

Írj egy kasszahoz_rendel nevű függvényt, amely egy olyan szöveget kap paraméterül,
mely pontosvesszővel elválasztott (egész) számokat tartalmaz! A függvény visszatérési értéke egy 2-dimenziós lista,
amely 2 részlistából áll: az első részlistába a páros, a második részlistába pedig a
páratlan sorszámok kerülnek növekvő sorrendben.
Példa:
Input: '42;38;45;40;41;39;44;43;46'
Return: [[38, 40, 42, 44, 46], [39, 41, 43, 45]]
Input: '12;16;14'
Return: [[12, 14, 16], []]
'''

def kasszahoz_rendel(karakter):
    szamok=[[],[]]
    lista=karakter.split(";")
    for elem in lista:
        elem = int(elem)
        if elem % 2 == 0:
            szamok[0].append(int(elem))
        else:
            szamok[1].append(int(elem))
    return szamok

def rendezes(lista):
    for elotte in range(len(lista[0])):
        for mogotte in range(elotte+1,len(lista[0])):
            if lista[0][elotte]>lista[0][mogotte]:
                temp=lista[0][elotte]
                lista[0][elotte]=lista[0][mogotte]
                lista[0][mogotte]=temp
    for elotte in range(len(lista[1])):
        for mogotte in range(elotte+1,len(lista[1])):
            if lista[1][elotte]>lista[1][mogotte]:
                temp=lista[1][elotte]
                lista[1][elotte]=lista[1][mogotte]
                lista[1][mogotte]=temp
    return lista

sztring="42;38;45;40;41;39;44;43;46"
print (rendezes(kasszahoz_rendel(sztring)))
