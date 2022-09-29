'''
Használja fel az előző gyakorlatokban definiált  függvényeket egy olyan script írására, ami ki tudja
szedni egy szövegből az összes nagybetűvel kezdődő szót.
'''

mondat= "Összes nagybetüvel Kezdődő szó visszaadása."

#1. megoldás
def listava_alakit(x):
    return x.split()

def nagybetüs_szo(x):
    lista=listava_alakit(x)
    for elem in lista:
        if elem == elem.capitalize():
            print (elem)
nagybetüs_szo(mondat)

#2.megoldás:
def listava_alakit_2(x):
    sztring=""
    szotar=[]
    for elem in x:
        if elem == " " or elem ==".":
            sztring += elem
            szotar.append(sztring)
            sztring=""
        else:
            sztring+=elem
    return (szotar)

def nagybetu(x):
    for elem in x:
        if elem == elem.capitalize():
            print (elem)

lista= listava_alakit_2(mondat)
nagybetu(lista)