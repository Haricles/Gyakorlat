'''
Írj egy programot, amely a main() függvényben generál egy véletlenszámot [1; 10] intervallumon és eltárolja azt egy
változóban. Egy másik függvény kérjen be a felhasználótól egy számot, és ezzel írja felül a main()
függvényben létrehozott változó értékét. A bekérés és felülírás mindaddig folytatódjon,
amíg a felhasználó 0-t nem ad meg!
'''
import random

def felüliras():
    return int(input("Kerek egy szamot:"))


def main():
    b= int(input("Kerem a szamot,hogy végre hajtsam a loopot! "))
    a = random.randint(1,10)
    while b != 0:
        print("Az 'a' valtozó értéke:", a)
        if b != 0:
            a = felüliras()
            b = int(input("Kerem a szamot,hogy végre hajtsam a loopot! "))
    print ("A kiértékeléskor az 'a' változó értéke:",a)




(main())
