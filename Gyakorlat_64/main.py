'''
Készíts egy programot, amely a felhasználó által megadott mondatról a mondatvégi jel alapján eldönti milyen fajtájú!
 (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)

'''
#1. megoldás
bemenet = input("Kerem a mondatot: ")
if "?" in bemenet:
    print ("Kérdő")
elif "!" in bemenet:
    print ("Felkiáltó/Felszólító")
elif "." in bemenet:
    print ("Kijelentő")

#2.megoldás
bemenet_2= input("Kerem a mondatot: ")
for elem in bemenet_2:
    if elem[-1]=="?":
        print ("Kérdő")
    elif elem[-1]=="!":
        print ("Felkiáltó/Felszólító")
    elif elem[-1] == ".":
        print("Kijelentő")





