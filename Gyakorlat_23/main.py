'''
Kérje a felhasználótól a nevét és a nemét. Ezektől az adatoktól függően irassa ki a felhasználó nevét és Úr-at vagy
Asszony-t.
'''

nev = input("Kerem a nevet: ")
nem = input("Kerem a nemét: ").lower()

if nem == "férfi":
    print(f"{nev} Úr")
if nem == "nő":
    print (f"{nev} Asszony")