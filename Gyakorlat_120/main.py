'''
Adott két függvény (y=2x+3 és y=3x+1), mindkettő értelmezési tartománya az egész számok [0;10] intervallumon.
A program készítsen egy-egy halmazt a függvények értékkészleteivel, írja ki ezeket a képernyőre,
majd jelenítse meg a halmazok metszetét, unióját és különbségét!
'''


def elso(x):
    return (2*x)+3

def masodik(x):
    return (3*x)+1

halmazom = set()
for elem in range(0,11):
    halmazom.add(elso(elem))

halmazom_2=set()
for elem in range(0,11):
    halmazom_2.add(masodik(elem))


print (halmazom)
print (halmazom_2)

print (halmazom & halmazom_2)
print (halmazom | halmazom_2)








































