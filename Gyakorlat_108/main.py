'''
Alakítsd át úgy a programot, hogy a koordinátapárok bekérése addig folytatódjon, míg a felhasználó
intervallumon kívüli értéket nem ad meg! A program minden bekérés után rajzolja ki a rácsot úgy,
hogy megjeleníti a már korábban megadott koordináták esetében is a '+' jelet!
'''
#Ezzel generálom le a kétdimenziós listát.
tarolo = [[],[],[]]
for elem in range(3):
    for i in range(3):
        list_elemei="0"
        tarolo[elem].append(list_elemei)

#Ez vissza jelzésnek van itt,hogy lássam jól működik a program.
for sor in range(len(tarolo)):
    for oszlop in range(len(tarolo)):
        print (f"({sor},{oszlop})","",end="")
    print ("")

def megjelenites():
#függvény ami +-t rajzol a megadott koordinátára.
    bemenet_1 = int(input("Kerem az első koordinátát: "))
    bemenet_2 = int(input("Kerem a második koordinátát: "))
    while bemenet_1<3 and bemenet_2 <3:
        for sor in range(len(tarolo)):
            for oszlop in range(len(tarolo)):
                if sor == bemenet_1 and oszlop == bemenet_2:
                    print("+", "", end="")

                else:
                    print("O", "", end="")
            print("")
        bemenet_1 = int(input("Kerem az első koordinátát: "))
        bemenet_2 = int(input("Kerem a második koordinátát: "))

megjelenites()