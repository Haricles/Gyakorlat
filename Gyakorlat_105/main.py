'''
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál,
és ezeket a listákat egy 'tarolo' nevű listába helyezi. A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
'''

import random

tarolo = [[],[],[],[]]
for elem in range(4):
    for j in range(3):
        a = random.randint(0, 25)
        tarolo[elem].append(a)

print (tarolo)


tarolo_2=[[random.randint(0,25) for elem in range(3)] for i in range(4)]
print(tarolo_2)
