'''
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat
több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a
kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg,
3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!
'''

def kerulet(a,b=0,c=0):
    if (c !=0) and (b !=0):
        return a+b+c
    if (c ==0) and (b !=0):
        return 2*(a+b)
    if (c ==0) and (b ==0):
        return 4*a

def kerulet_2(x,*args):
    a = 0
    b=x
    for elem in args:
        a +=1
        b += elem
    if a == 0:
        print ("Négyszög")
        return 4*x
    elif a == 1:
        print("Téglalap")
        return 2*b
    else:
        if a == 2:
            print("Háromszög")
        else:
            print ("Sokszög")
        return b


print (kerulet(5))
print (kerulet(5,2))
print (kerulet(5,2,3))

print (kerulet_2(1))
print (kerulet_2(1,2))
print (kerulet_2(1,2,4))
print (kerulet_2(5,2,3,6,7,9))




