'''
Pontszám konvertálás iskolai jeggyé.
'''

pontszam = int(input("Kerem a pontszamod: "))

if pontszam < 40:
    print ("Az osztályzatod: E")
elif 40 <= pontszam < 50:
    print ("Az osztályzatod: D")
elif 50 <= pontszam < 60:
    print ("Az osztályzatod: C")
elif 60 <= pontszam < 80:
    print ("Az osztályzatod: B")
else:
    print ("Az osztályzatod: A")