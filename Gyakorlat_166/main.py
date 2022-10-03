'''
Írjon egy scriptet, ami egy szövegfileban megszámolja a szavakat.
'''
osszeg=0
with open("valami.txt","r",encoding="utf-8") as file:
    for elem in file:
        sor = elem.strip()
        sor_2 = sor.split()
        osszeg+=len(sor_2)
print (osszeg)











