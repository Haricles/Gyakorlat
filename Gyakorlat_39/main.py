'''
Készíts egy programot,amely az alábbi példa alapján
rajzol a képernyőre egy pocak szerű alakzatot!

  O
  O O
  O O O
  O O O O
  O O O O
  O O O
  O O
  O
'''
sor_1=0
darab_1=0
while sor_1 <4:
    oszlop =0
    while oszlop <= darab_1:
        print ("0",end="")
        oszlop +=1
    print ("")
    darab_1 += 1
    sor_1 += 1
sor_2=0
darab_2=3
while sor_2 <4:
    oszlop =0
    while oszlop <= darab_2:
        print ("0",end="")
        oszlop +=1
    print ("")
    darab_2 -= 1
    sor_2 += 1




