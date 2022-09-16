'''
Írj egy programot, amely a main() függvényben egy lista formájában eltárolja az 'a', 'b' és 'c' betűket!
Egy másik függvény kérjen be a felhasználótól három betűt, és ezzel írja felül a main() függvényben
létrehozott lista tartalmát. A bekérés és felülírás mindaddig folytatódjon, amíg a
felhasználó három azonos betűt nem ad meg!

'''

def betükero(lista):
    lista[0]= str(input("Kerem az első betüt: "))
    lista[1] = str(input("Kerem a második betüt: "))
    lista[2] = str(input("Kerem a harmadik betüt: "))
    return lista

def main():
    betük = ["a","b","c"]
    while betük[0] != betük[1] != betük[2]:
        betük = betükero(betük)
        print("Jelenlegi betük: ",betük)
    print (betük)

main()