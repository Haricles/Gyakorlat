'''
Béla egy online játékkal játszik. A játékban talált egy bugot, amit kihasználva többször is be tud lépni a
játékba ugyanazzal a felhasználónévvel. A játékostársai ezt nem tartják tisztességesnek,
ezért úgy döntenek, hogy Bélát kirúgják a játékból.

Írj egy belat_kirug nevű függvényt, amely egy listát kap paraméterül, ami a játékosok neveit tartalmazza (stringek).
A függvény távolítsa el a listából az EpicBela20 játékosnév összes előfordulását,
majd térjen vissza az így kapott listával!

Input: ['EpicBela20', 'python4life', 'EpicBela20', 'EpicBela20', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']
Return: ['python4life', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']
'''
#1.megoldás
def belat_kirug(lista):
    uj_lista=[]
    for elem in lista:
        if elem != "EpicBela20":
            uj_lista.append(elem)
    return uj_lista

#2.megoldás:
def belat_kirug_2(lista):
    while "EpicBela20" in lista:
        lista.remove("EpicBela20")
    return lista

bemenet=['EpicBela20', 'python4life', 'EpicBela20', 'EpicBela20', 'kalkEasy', 'varj_ez_nem_is_csgo', 'sajt42']

print (belat_kirug_2(bemenet))
print (belat_kirug(bemenet))