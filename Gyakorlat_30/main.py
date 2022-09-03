'''
Definiáljon egy karakterSzam(ca,ch) függvényt ami visszadja a ch stringben előfordulő ca karakterek számát.
Pl: print karakterSzam("e","Cette phrase est un exemple")-nél 7-et kell kapnunk.
'''


def karakterSzam(ca,ch):
    return (ch.count(ca))

print (karakterSzam("e","Cette phrase est un exemple"))
