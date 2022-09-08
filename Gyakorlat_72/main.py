'''
Az előbbi programot módosítsd úgy, hogy csak a 3 betűnél hosszabb szavak kerülnek átalakítva a másik listába!
'''


lista_01 = ["alma","körte","répa","krumpli","gáz","paradicsom","paprika","vaj","kő"]
lista_02= [elem.capitalize() for elem in lista_01 if len(elem) <=3]
print(lista_01)
print (lista_02)

