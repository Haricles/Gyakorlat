'''
Az előző lecke 1. feladatában szereplő adatokat olvassa be a program, és tárolja el egy olyan listában,
amelynek az elemei szótárak. Ár szerint rendezve jelenítse meg az egyes árucikkek jellemzőit!
A rendezéshez használj egy arat_visszaad() nevű függvényt!
'''

lista= []
with open("myfile.txt","r",encoding="utf-8") as file:
    for elem in file:
        szotar = {}
        sor= elem.strip()
        sor_2=sor.split(";")
        szotar["Típus"]=sor_2[0]
        szotar["Bútor"]=sor_2[1]
        szotar["Osztály"]=sor_2[2]
        szotar["ár"]=int(sor_2[3])
        szotar["raktáron"]=sor_2[4]
        lista.append(szotar)

def arat_visszaad(x):
    return x["ár"]

lista.sort(key=arat_visszaad)
print ("Növekvő sorrend:",lista)
lista.sort(key=arat_visszaad,reverse=True)
print ("Csökkenő sorrend:",lista)







































































