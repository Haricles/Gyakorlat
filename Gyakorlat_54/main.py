'''
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását
(fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!

'''

#1. megoldás
import  random

erme = ["fej","írás"]
dobasok = random.choice(erme)

dobas = input("Fej vagy írás?")

if dobasok == dobas:
    print ("Eltaláltad!")
else:
    print ("Sajnos nem találtad el.")



