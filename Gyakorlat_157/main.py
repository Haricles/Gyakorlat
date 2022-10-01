'''
Írjon egy függvényt, aminek akkor « igaz » a visszaérési értéke, ha az argumentuma egy szám.
'''



def szam(x):
    i=1
    for elem in str(x):
        if (ord(elem) > 48) and (ord(elem) < 57):
            i+=1
        else:
            break
    if i < len(str(x)):
        print ("Ez betü")
    else:
        print ("EZ szám!")

szam(54)