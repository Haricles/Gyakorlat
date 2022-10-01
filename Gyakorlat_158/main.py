'''
Írjon egy függvényt, ami az argumentumaként megadott mondatban lévő nagybetűk számát adja meg
visszaérési értékként.
'''


def nagybetu_szama(x):
    i=0
    for elem in x:
        if ord(elem) >= 65 and ord(elem) <= 90:
            i+=1
    return i

a= "Volt Egyszer EGy VadNyugat."


print (nagybetu_szama(a))