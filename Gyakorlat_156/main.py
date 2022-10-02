'''
Írjon egy függvényt, aminek akkor « igaz » a visszaérési értéke, ha az argumentuma egy alfabetikus
karakter (nagy vagy kisbetű). Alkalmazza ebben az új függvényben az előzőekben definiált kisbetu()
és nagybetu() függvényeket
'''

def nagybetu_2(x):
    i=0
    for elem in x:
        if (ord(elem) >= 65) and (ord(elem) <=90):
            break
        else:
            i+=1
    if i < len(x):
        return True
    else:
        return False

def kisbetu_2(x):
    i = 0
    for elem in x:
        if (ord(elem)>=97) and (ord(elem) <=122):
            break
        else:
            i+=1
    if i < len(x):
        return True
    else:
        return False

def kis_nagybetu_2(x):
    i=0
    for elem in x:
        if nagybetu_2(elem) or kisbetu_2(elem):
            break
        else:
            i+=1
    if i < len(x):
        return True
    else:
        return False

print (kis_nagybetu_2("432343"))