'''
Írjon egy programot, ami m/sec és km/h-ba számolja át a felhasználó által mérföld/h-ban megadott sebességet.
'''

bemenet = int(input("Kerem a mérföld/h-t: "))

km_h = bemenet * 1.609
m_s = km_h // 3.6

print (f"A megadott mérföld/h az {km_h} km/h-nak és {m_s} m/s-nak felel meg." )