'''

Készíts egy rövid programot ,amely 1 és 3 között generál véletlenszámot,majd összehasonlítja ezt a felhasználó által
megadott,szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
'''


import random

randomszam= random.randint(1,3)
felhasznaloszama= int(input("Kerem a szamod 1-3 között: "))
if randomszam == felhasznaloszama:
    print ("Eltaláltad a random számot."," A random szám: ",randomszam)
else:
    print ("Sajnos ez most nem sikerült.","A random szám: ",randomszam)
