# Írjon egy programot ami a kiíratja a sakktábla 64 kockájának mindegyikére elhelyezett rizsszemek számát.
# 1.kocka 1szem,2.kocka 2szem,3.kocka 4szem,és így tovább 64-ig.

osszeg = 1
for elem in range(0,64):
    osszeg = osszeg + elem
    print (osszeg)