'''
Írjon egy scriptet, ami megszámolja egy szövegfileban a numerikus karaktereket tartalmazó sorokat.
'''



szamlalo=0
with open("valami.txt","r",encoding="utf-8") as file:
    for elem in file:
        lista= elem.strip().split()
        szamlalo += len(lista)
print (szamlalo)













