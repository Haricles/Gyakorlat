'''
Ugyanennek a relációnak az alapján írjon egy függvényt, ami valamennyi kisbetűt nagybetűvé alakít át
és viszont (az argumentumként megadott mondatban).

'''

def kisbetu_nagybetuve(x):
    sztring = ""
    for elem in x:
        if (ord(elem) >= 97) and (ord(elem) <= 122):
            elem = elem.upper()
            sztring+=elem
        else:
            sztring+=elem
    print (sztring)

mondat = "Volt egySzer egy VaDnyugat."

kisbetu_nagybetuve(mondat)

