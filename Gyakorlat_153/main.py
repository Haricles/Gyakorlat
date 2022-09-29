'''
Írjon egy függvényt, ami egy mondatot szavakból álló listává alakít át.
'''

mondat= "Volt egyszer egy vadnyugat"

def listava_alakit(x):
    return x.split()


print (listava_alakit(mondat))