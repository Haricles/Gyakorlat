# Írjon egy programot ami kiír egy 12 számból álló sorozatot,aminek minden tagja vagy egyenlő az előző taggal
# vagy annak a háromszorosa.

osszeg = 0
for i in range(1,13):
    osszeg= osszeg+i
    print (f"{osszeg}")