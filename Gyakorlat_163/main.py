'''
Írjon egy függvényt, ami visszatérési értékként megadja egy adott mondatban a magánhangzók számát.
'''

def maganhangzok(x):
    maghang=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
    szamlalo=0
    for elem in x.lower():
        if elem in maghang:
            szamlalo+=1
    return szamlalo


print (maganhangzok("volt egyszer egy vadnyugat."))









