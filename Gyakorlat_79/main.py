'''
A program tároljon el egy szót egy változóban. A felhasználó adjon meg egy betűt, amiről a program döntse el,
hogy előfordul-e a szóban! Az eredményről tájékoztassa a felhasználót, és írja ki a tárolt szót is!
'''

a = "karalábé"
bemenet = input("Kerek egy betüt: ")
if bemenet in a:
    print ("Benne van!","A tárolt szó:",a)
else:
    print ("Nincs benne!","A tárolt szó:",a)










