'''
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként
átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False!
A program tartalmazza a függvény hívását is!

'''
mylist=[53,3,7,9]
mylist_2=[2,4,5,6,3]
def paros_e(lista):
    for elem in lista:
        if elem % 2 == 0:
            return True
        else:
            return False
print (paros_e(mylist))
print (paros_e(mylist_2))



