'''

Készíts egy programot,amely a felhasználótól bekér egy egész számot,majd megvizsgálja,hogy a megadott szám
-pozitív páros vagy
-negatív páratlan

'''

a = int(input("Kérek egy számot: "))
if a % 2 == 0 and a > 0:
    print ("Ez pozitív páros szám")
elif a % 2 == 1 and a < 0:
    print ("Ez negatív páratlan szám")
else:
    print ("Sajnos ez a szám vagy pozitív páratlan vagy negatív páros.")


