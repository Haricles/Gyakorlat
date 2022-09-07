'''
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín
már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás
mellé vesszővel elválasztva a lista által tartalmazott színeket!
'''

paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

bemenet = input("Kerek egy színt! ")
if bemenet in paletta:
    print ("Már szerepel benne! ")
else:
    print ("Még nincs benne!")

print ("A lista szinei: ")
for elem in paletta:
    print (elem,"",end=",")




