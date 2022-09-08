'''
Készíts egy programot, amely sztringeket tartalmazó listaelemek leképezését valósítja meg.
A leképezéshez a sztringek metódusait ezen az oldalon bemutató listából válassz egyet!
A program írja ki az eredeti és a generált listát is a képernyőre!


'''


lista_01 = ["alma","körte","répa","krumpli","gáz","paradicsom","paprika","vaj","kő"]
lista_02= [elem.replace("","-") for elem in lista_01 if len(elem) <=3]
print(lista_01)
print (lista_02)

