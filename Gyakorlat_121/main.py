'''
Írj egy programot, amely a felhasználótól bekér egy RGB színkód három összetvőjét! A program állapítsa meg és
írja ki a képernyőre, hogy az adott szín tartalmaz-e zöld komponenst, illetve melyik komponensből van a legtöbb,
és melyikből a legkevesebb!
'''

rgb=(320,2,211)
r,g,b=rgb
#1. megoldás:
def legtöbb(a):
    if r > g and r > b:
        print ("A red színből van a legtöbb!")
    elif g > r and g > b:
        print (" A green szinből van a legtöbb!")
    elif b > r and b > g:
        print ("A blue színből van a legtöbb!")

def legkevesebb(a):
    if r < g and r < b:
        print ("A red színből van a legkevesebb!")
    elif g < r and g < b:
        print (" A green szinből van a legkevesebb!")
    elif b < r and b < g:
        print ("A blue színből van a legkevesebb!")

def van_benne(a):
    if r == 0:
        print ("Nincs benne red.")
    elif g == 0:
        print ("Nincs benne green.")
    elif b==0:
        print ("Nincs benne blue.")

legtöbb(rgb)
legkevesebb(rgb)
van_benne(rgb)
#1.megoldás vége.

#2.megoldás
rgb2=(300,10,211)
r2,g2,b2=rgb2

def legtöbb(a):
    if r2 > g2 and r2 > b2:
        print ("A red színből van a legtöbb!")
    elif g2 > r2 and g2 > b2:
        print (" A green szinből van a legtöbb!")
    elif b2 > r2 and b2 > g2:
        print ("A blue színből van a legtöbb!")

def legkevesebb(a):
    if r2 < g2 and r2 < b2:
        print ("A red színből van a legkevesebb!")
    elif g2 < r2 and g2 < b2:
        if g2==0:
            print ("Nincs benne green ezért ebből van a legkevesebb!")
        else:
            print (" A green szinből van a legkevesebb!")
    elif b2 < r2 and b2 < g2:
        print ("A blue színből van a legkevesebb!")

legtöbb(rgb2)
legkevesebb(rgb2)






































