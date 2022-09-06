'''

Készíts egy programot! A gép "gondol" egy számra 1 és 5 között vagyis egy változóban tárolj egy ilyen számot!
Azután a program bekér egy számot a felhasználótól,majd kiírja,hogy ez a szám egyenlő-e a gép által "gondolt" számmal,
vagy annál kisebb,illetve nagyobb.
'''

import random

a = random.randint(1,5)
b = int(input("Gondoltam egy számra 1 és 5 között. Próbáld meg kitalálni. Kérem a tipped: "))
if a<b:
    print ("Sajnos a számod kisebb mint a gondolt szám.")
elif a>b:
    print ("Sajnos a számod nagyobb mint a gondolt szám.")
else:
    print ("Gratulálok nyertél!")