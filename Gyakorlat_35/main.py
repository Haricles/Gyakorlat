'''
Módosítsa az egyik előző példában definiált dobozTerfogat(x1,x2,x3) függvényt úgy hogy 3,2,1 argumentummal vagy
akár argumentum nélkül is lehessen hívni. Alapértelmezetten az argumentum értéke legyen 10.
'''

def dobozTerfogat(x1=10,x2=10,x3=10):
    return (x1*x2)*x3

print (dobozTerfogat())
print (dobozTerfogat(5.2))
print (dobozTerfogat(5.2,3))