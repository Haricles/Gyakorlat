'''
Írjon egy függvényt, ami felcseréli egy szótárban a kulcsokat és az értékeket (ami például lehetővé teszi,
hogy egy angol/francia szótárat francia/angol szótárrá alakítsunk).
(Feltételezzük, hogy a szótár nem tartalmaz több azonos értéket).
'''

szotar={"Hungary":"Magyar"}
print (szotar)
print (szotar["Hungary"])

uj_szotar={}
for kulcs,ertek in szotar.items():
    uj_szotar[ertek]=kulcs
    print (uj_szotar)
print (uj_szotar["Magyar"])