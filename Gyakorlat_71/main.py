'''
Készíts egy programot, amely listaelemek leképezésével megvalósítja a következő funkciót: egy szavakat tartalmazó
lista elemeiből generál egy másik listát, amelyben az eredeti szavak csupa nagybetűs formában szerepelnek!
 A program írja ki az eredeti és a generált listát is a képernyőre!
'''


lista_01 = ["alma","körte","répa","krumpli","paradicsom","paprika"]
lista_02= [elem.capitalize() for elem in lista_01]
print(lista_01)
print (lista_02)

