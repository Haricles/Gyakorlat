'''
Definiáljon egy dobozTerfogat(x1,x2,x3) nevű függvényt,ami egy parallelepipedon térfogatát adja vissza aminek a
méretetit az x1,x2,x3 argumentumokban adjuk meg. print(dobozTerfogat(5.2,7.7,3.3)) utasítás eredményeként 132.13-at
kell kapnunk.
'''

def dobozTerfogat(x1,x2,x3):
    return (x1*x2)*x3

print (dobozTerfogat(5.2,7.7,3.3))