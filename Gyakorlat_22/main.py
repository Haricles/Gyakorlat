'''
Írjon egy programot ami adott a és b korlátok esetén összeadja a 3 és 5 korlátok közé eső többszoroseit.
Vegyük peldaul az a =0 és b= 32-t az eredmenynek 0+15+30=45-nek kell lennie
'''

a= 0
b = 32
osszeg = 0

for elem in range(a,b+1):
    if elem % 3==0 and elem % 5 ==0:
        osszeg = osszeg+elem
        print (elem,"",end="")
print ("=",osszeg)

#Módosítsa úgy a programot,hogy adja össze 3-nak vagy az 5-nek az a és b határok közé eső többszöröseit.
# Eredmenynek ezt kell látni: 0+3+5+6+9+10+12... stb

osszeg_2=0
for elem in range(a,b+1):
    if elem % 3 == 0 or elem % 5 ==0:
        osszeg_2 = osszeg_2+elem
        print (osszeg_2,"",end="")