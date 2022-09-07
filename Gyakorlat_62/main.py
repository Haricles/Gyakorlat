'''
Az előző programot alakítsd át úgy, hogy a feltételeknek megfelelő szavak kerüljenek rögzítésre egy
másik listában is, és ez utóbbi listát írja ki a program a képernyőre!

'''
szavak_2 = []
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for elem in szavak:
    if elem[0] == "t" or elem[0] == "T":
        szavak_2.append(elem)
print (szavak_2)






