'''
Készíts egy programot,amely egymásba ágyazott ciklusok segítségével rajzolja ki egy 7x7-es mezőben az alábbi
alakzatot:

0 . . . . . 0
. 0 . . . 0 .
. . 0 . 0 . .
. . . 0 . . .
. . 0 . 0 . .
. 0 . . . 0 .
0 . . . . . 0

'''
sor=0
while sor < 7:
    oszlop = 0
    while oszlop < 7:
        print (f"({sor+oszlop:2})","",end="")
        oszlop+=1
    print ("")
    sor += 1

sor=0
while sor < 7:
    oszlop = 0
    while oszlop < 7:
        if oszlop == sor or oszlop+sor==6:
            print ("0","",end="")

        else:
            print (".","",end="")
        oszlop+=1
    print ("")
    sor += 1