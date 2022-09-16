'''
Írjon egy dobozTerfogat(x1,x2,x3) nevű függvényt olymódon,hogy 3,2, vagy 1 argumentummal lehessen hívni.
Ha egy argumentumot használunk,akkor a dobozt kockának tekintjük (az argumentum a kocka oldala). Ha két argumentumot
használunk ,akkor a dobozt négyet alapú prizmának tekintjük. (Ebben az esetben az első argumentum a négyzet oldala
és a második a prizma magassága). Ha három argumentumot használunk,akkor a dobozt parallelepipedonnak tekintjük.

print (dobozTerfogat(5.2))              eredmény : 140.608
print (dobozTerfogat(5.2,3))            eredmény : 82.12
print (dobozTerfogat(5.2,3,7.4))        eredmény : 115.44

'''

def dobozTerfogat(x1,x2=0,x3=0):
    if (x2 != 0) and (x3 != 0):
        print ("Parallelepipedon!")
        return (x1*x2)*x3
    elif x2 != 0:
        print ("Négyzet alapú prizma!")
        return (x1**2)*x2
    else:
        print ("Kocka!")
        return x1**3

print (dobozTerfogat(5.2))
print (dobozTerfogat(5.2,3))
print (dobozTerfogat(5.2,3,7.4))