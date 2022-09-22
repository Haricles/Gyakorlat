'''
Az alábbi sorokat másold be egy .txt kiterjesztésű fájlba!
Készíts egy programot, amely ezen forrásfájlban szereplő adatokat beolvassa és eltárolja!
A program válogassa ki egy külön listába, a raktáron lévő bútorokat, majd jelenítse meg a lista tartalmát!
'''
lista=[]
with open("myfile.txt","r",encoding="utf-8") as myfile:
    for sor in myfile:
        adat= sor.strip().split(";")
        lista.append(adat[1])
print (lista)

























































