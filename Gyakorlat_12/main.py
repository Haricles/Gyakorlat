# Írjon egy programot ami egy új valtozóba másol át egy karakterláncot úgy,hogy csillagot szúr be a karakterek közé.
# PL: gaston-ból g*a*s*t*o*n lesz.

szo = "gaston"
for betu in range(len(szo)):
    print (szo[betu] + "*","",end="")

for betu in szo:
    print (betu + "*","",end="")