'''
Torpedó játék egyszerűsített változata. A játéktér legyen egy 3x3-as négyzetalakú rács, amiben az oszlopokat betűk
(A, B, C), a sorokat számok (1, 2, 3) jelölik. A program helyezzen el egy darab egy egység kiterjedésű hajót a
játéktérben véletlenszerűen (Pl: B2). A játékos próbálja meg kitalálni a hajó pozícióját újabb és újabb
tippek megadásával. A játék végén a program azt is írja ki a képernyőre, hogy hány próbálkozásból tudta a
játékos kitalálni a pozíciót!
'''

sor = 1
while sor <= 3:
    elem = ["A","B","C"]
    for oszlop in elem:
        print (f"({sor},{oszlop})",end="")
    sor +=1
    print ("")


for sor in range(1,4):
    elem = ["A","B","C"]
    for oszlop in elem:
        if sor == 2 and oszlop =="B":
            print ("+",end="")
        else:
            print (".",end="")
    print ("")












