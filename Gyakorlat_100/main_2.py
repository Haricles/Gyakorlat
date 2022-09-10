'''
Írj egy programot, amely a main() függvényben generál egy véletlenszámot [1; 10] intervallumon és eltárolja azt egy
változóban. Egy másik függvény kérjen be a felhasználótól egy számot, és ezzel írja felül a main()
függvényben létrehozott változó értékét. A bekérés és felülírás mindaddig folytatódjon,
amíg a felhasználó 0-t nem ad meg!
'''
import random

def felüliras(b):
    return int(b)

def main():
    a = random.randint(1,10)
    b = a
    while (a != 0) and (b!=0):
        b = int(input("Kerek egy számot: "))
        if b != 0:
            a = felüliras(b)
        print("Az 'a' valtozó értéke:", a)
    print ("A kiértékeléskor az 'a' változó értéke:",a)



(main())
