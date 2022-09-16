'''
Írj egy programot, amely létrehoz egy 'tarolo' nevű listát, amelynek a három listaeleme egy-egy három elemű lista!
Ezen beágyazott listák elemei legyenek sztring formátumban: 'O '.
A program járja be a listákat, és jelenítse meg a bennük tárolt értékeket úgy, hogy azok egy 3x3-as rácsot adjanak ki.
A rács képernyőn való megjelenítéséről egy eljárás gondoskodjon!!
'''

tarolo = [[],[],[]]
for elem in range(3):
    for i in range(3):
        list_elemei="0"
        tarolo[elem].append(list_elemei)
print (tarolo)

def megjelenites():
    for elem in tarolo:
        print (elem[0],elem[1],elem[2])




megjelenites()