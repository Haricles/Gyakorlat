'''
Tökéletesítse  az előző gyakorlat függvényét úgy, hogy egy harmadik paramétert ad hozzá : azt az
indexet, amelyiktől kezdve keresni kell a karakterláncban. Így például a következő utasításnak : 15-öt
kell kiírni (és nem 4-et !)
print megtalal("César & Cléopâtre", "r", 5)

'''

def megtalal(sztring,megtalalando,ettől):
    if megtalalando in sztring:
        return sztring[ettől:].index(megtalalando)+ettől
    else:
        return -1

print (megtalal("César & Cléopâtre", "r", 5))





































