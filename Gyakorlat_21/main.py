'''
Írjon egy programot, ami értékeket tesz egy listába. Ennek a programnak ciklusban kell működni úgy hogy
mindaddig kéri az értékeket amíg a felhasználó úgy nem dönt hogy befejezésként entert üt. A program a lista kiírásával
fejeződik be.
'''


t1 = []
bemenet = None
while bemenet != "":
    bemenet = (input("Kerem a szamot: "))
    if bemenet != "":
        t1.append(int(bemenet))

print (t1)

