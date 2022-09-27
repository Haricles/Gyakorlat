'''
Írjon egy scriptet,ami összehasonlítja két fájl tartalmát és jelzi az első eltérést.
'''


file_1_tomb=[]

with open("valami.txt","r",encoding="utf-8") as file_1:
    for elem in file_1:
        file_1_tomb.append(elem.strip())

z=0
with open("valami2.txt","r",encoding="utf-8") as file_2:
    for elem in file_2:
        if elem.strip() != file_1_tomb[z]:
            print (elem.strip())
            break
        z+=1








































