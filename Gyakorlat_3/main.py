#Írj egy programot,amit euróban kifejezett pénzösszegeket kanadai dollárba vált át és az \n
# eredményt egy táblázatba írja ki. A táblázatban a pénzösszegeket geometriai haladvány szerint növekedjen \n
# úgy mint az alábbi példában: 1 euro = 1.65 dollar,2 euro = 3.3 dollar 4 euro = 6.6 dollar , 8 euro = 13.2 dollar

a = 1
valtoszam = 1.65
while a< 16384:
    print (a,"=",a*valtoszam)
    a *= 2
