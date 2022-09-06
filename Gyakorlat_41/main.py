'''
Készíts egy programot,amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 5x5-ös mezőben az alábbi
alakzatot:

0 . . . .
. 0 . . .
. . 0 . .
. . . 0 .
. . . . 0

'''
sor=0
while sor < 5:
    oszlop = 0
    while oszlop < 5:
        print (f"({sor},{oszlop})","",end="")
        oszlop+=1
    print ("")
    sor += 1


sor=0
while sor < 5:
    oszlop = 0
    while oszlop < 5:
        if oszlop == sor:
            print ("0","",end="")
        else:
            print (".","",end="")
        oszlop+=1
    print ("")
    sor += 1