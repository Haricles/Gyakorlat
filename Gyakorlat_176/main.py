'''
Rendelkezésére   áll   valamilyen   (nem   túl   nagy)   szövegfile.  Írjon   egy   scriptet,   ami   megszámolja   a
szövegben   az   abc   betűinek   az   előfordulását   (az   ékezetes   karakterek   problémáját   nem   vesszük
figyelembe).
'''

with open("bemenet.txt","r",encoding="utf-8") as file:
    for elem in file:
        sor = elem.strip().lower()

betuk={}
for elem in sor:
    betuk[elem]=betuk.get(elem,0)+1

print (betuk)

