'''
A "Próbáld ki!" gombra kattintva elérhető egy program, ami egy eljárás segítségével kirajzol a képernyőre
egy 6x3-as mezőt.
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az
adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O

'''
#1. megoldás (itt nem néztem meg jól a feladatot és a fő programot is megcsináltam)
def mezot_rajzol(a,b):
    sor = 1
    while sor <= 3:
        oszlop = 1
        while oszlop <= 6:
            if sor == a and oszlop== b:
                print ("+","",end="")
            else:
                print ("0","",end="")
            oszlop +=1
        sor +=1
        print ("")

mezot_rajzol(2,2)
print ("-----------")
#2. megoldás
def mezot_rajzol_2(a,b):
    for sor in range(3):
        for oszlop in range(6):
            if sor == a and oszlop == b:
                print('+',"",end='')
            else:
                print ("0","",end="")
        print()

mezot_rajzol_2(2,1)






