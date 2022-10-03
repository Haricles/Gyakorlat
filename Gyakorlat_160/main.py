'''
Az előző gyakorlatban megtalált reláció alapján írjon egy függvényt, ami egy mondat valamennyi
karakterét kisbetűre írja át.

'''

mondat="Volt egySzer egy VaDnyugat."

#97-től 122-ig

sztring=""
for elem in mondat:
    if (ord(elem) >= 65) and (ord(elem) <= 90):
        elem = elem.lower()
        sztring+=elem
    else:
        sztring+=elem

print (sztring)


