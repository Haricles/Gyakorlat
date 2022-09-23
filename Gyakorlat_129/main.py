'''
Alakítsd át az előző programot úgy, hogy a rendezéshez lambda függvényt haszáljon!

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


lista.sort(key=lambda x: x["ár"])
print ("Növekvő sorrend:",lista)
lista.sort(key=lambda x: x["ár"],reverse=True)
print ("Csökkenő sorrend:",lista)







































































