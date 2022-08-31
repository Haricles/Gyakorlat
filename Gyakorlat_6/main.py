# Írjon egy programot ami kiíratja a 7-es szorzótábla első 20 tagját,csillaggal jelölve azokat,amelyek 3-nak
# többszörösei. Pl: 7 14 21 * 28 35 42 * 49


for i in range(1,8):
    a = i*7
    print (a,"",end="")
    if a % 3 ==0:
        print ("*","",end="")