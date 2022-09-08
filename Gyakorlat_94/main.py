'''
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket
(egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!

'''
mylist=[2,5,7,8,3]
def osszegzo(lista):
    osszeg = 0
    for elem in lista:
        osszeg = osszeg + elem
    return osszeg

print (osszegzo([23,45,65,23,72,1]))
print (osszegzo(mylist))



