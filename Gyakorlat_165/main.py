'''
Írjon egy scriptet, ami egy szövegfileban megszámolja a szavakat.
'''

szamlalo=0
with open("valami.txt","r",encoding="utf-8") as file:
    for elem in file:
        lista= elem.strip().split()
        szamlalo += len(lista)
print (szamlalo)


























