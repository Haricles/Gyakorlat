'''
Készíts egy rövid programot amely kommentként tartalmazza a program funckiójának leírását,konstansként tárolja a pi
értékét,egy másik változóban tárolja a kör sugarának nagyságát,kiszámolja és a képernyőre kiírja a kör kerületét és
területét!
'''

import math

pi_ertek = math.pi      # lehetne simán 3.14 az math.pi helyett,de így pontosabb eredményt kapok.
r = 3
k = 2*r*pi_ertek
t= (r**2)*pi_ertek
print (f"A kör kerülete: {k} és a területe: {t}")



