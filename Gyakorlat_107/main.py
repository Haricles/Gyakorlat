'''
Egészítsd ki úgy a programot, hogy a felhasználó megadhasson egy koordinátát (a bal felső rácspont koordinátája (0;0),
a jobb alsó pedig (2;2)), és ekkor a program rajzolja ki úgy a 3x3-as rácsot,
hogy a megadott koordinátán 'O ' helyett, '+ ' legyen!
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
    for sor in range(len(tarolo)):
        for oszlop in range(len(tarolo)):
            if sor == bemenet_1 and oszlop == bemenet_2:
                print("+", "", end="")
            else:
                print("O", "", end="")
        print("")

megjelenites()