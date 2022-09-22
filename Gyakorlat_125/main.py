'''
Készíts egy programot, ami a rendszámokban előforduló karkatereket helyettesíti
'|' jellel a betűket,
'*' jellel a számokat
az alábbiaknak megfelelően:

rendszamok = ['ABC123', 'ABCD777', 'WN25L']
atalakitva = ['|||***', '||||***', '||**|']

'''
rendszamok = ['ABC123', 'ABCD777', 'WN25L']
abc= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#1. megoldás
atalakitva=[]
for elem in rendszamok:
    valtozo = ""
    for i in elem:
        if i in abc:
            valtozo+= "|"
        else:
            valtozo+= "*"
    atalakitva.append(valtozo)
print (atalakitva)
#1.megoldás vége.
#2. megoldás
atalakitva_2=[]
for elem in rendszamok:
    ertek=""
    for i in elem:
        if i > chr(65) and i < chr(90):
            ertek += "|"
        else:
            ertek += "*"
    atalakitva_2.append(ertek)

print (atalakitva_2)
























































