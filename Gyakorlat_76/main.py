'''
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be,
amikor a felhasználó intervallumon kívüli értéket ad meg!
A program írja ki a megadott intervallumba eső számokat és az összegüket!
'''

a = 0
osszeg = 0
while -5 <= a <= 5:
    a = int(input("Kerek egész szamokt -5-5 intervallumon! "))
    if -5 <= a <= 5:
        osszeg = osszeg + a
    print (osszeg)







