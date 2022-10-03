'''
Írjon egy scriptet, ami megszámolja egy szövegfileban a numerikus karaktereket tartalmazó sorokat.
'''


szamok=["0","1","2","3","4","5","6","7","8","9"]
szamlalo=0
with open("valami.txt","r",encoding="utf-8") as file:
    for elem in file:
        sor= elem.strip()
        for elem in sor:
            if elem in szamok:
                szamlalo+=1
                break

print ("Numerikus karaktereket tartalmazó sorok száma:",szamlalo)





