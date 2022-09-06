'''
Készítsen egy rövid programot,amely a felhasználótól bekéri a kör sugarát és ennek alapján kiszámolja kör kerületét
és területét.
'''

import math

pi_ertek = math.pi      # lehetne simán 3.14 az math.pi helyett,de így pontosabb eredményt kapok.
r = int(input("Kerem a kör sugarat: "))
k = 2*r*pi_ertek
t= (r**2)*pi_ertek
print (f"A kör kerülete: {k} és a területe: {t}")



