'''
Tegyük fel,hogy rendelkezésére áll egy szövegfile,ami különböző hosszúságú mondatokat tartalmaz.
Írjon egy scriptet ami megkeresei és kiírja a leghosszabb mondatot.
'''


with open("Atlas-enUS.lua","r",encoding="utf-8") as olvaso:
    lista = []
    for sor in olvaso:
        lista.append(sor)
    legnagyobb = lista[0]
    for elem in lista:
        if len(legnagyobb) < len(elem):
            legnagyobb = elem
    print ("A leghosszabb mondat: ",legnagyobb)




