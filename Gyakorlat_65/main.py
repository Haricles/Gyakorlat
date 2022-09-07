'''
Az előbbi programot módosítsd úgy, hogy újabb és újabb mondatot kérjen be a program
(amig a felhasználó csak egy ENTER-t nem üt),
majd állapítsa meg, és írja ki mineden egyes alkalommal a mondat fajtáját!

'''

bemenet_2 = None
while bemenet_2 != "":
    bemenet_2= input("Kerem a mondatot: ")
    for elem in bemenet_2:
        if elem[-1]=="?":
            print ("Kérdő")
        elif elem[-1]=="!":
            print ("Felkiáltó/Felszólító")
        elif elem[-1] == ".":
            print("Kijelentő")





