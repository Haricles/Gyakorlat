'''
Írjon egy scriptet ami automatikusan létrehoz egy szövegfile-t ami 2-30 szorzótáblákat tartalmazza
(mindegyik szorzótábla csak 20 tagot tartalmazzon).
'''


with open("szorzotabla.txt","a",encoding="utf-8") as szorzotabla:

    for elem in range(1,21):
        for j in range(2,31):
            v= (str(elem*j))
            szorzotabla.write(v+",")
        szorzotabla.write("\n")





