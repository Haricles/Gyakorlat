'''
Tünde szeret olvasni, így a polcán is sok könyv van. Egyik nap Tünde rendet rak a lakásában, és a könyveit is rendezi.
Írj egy konyveket_rendez nevű függvényt, amely egy könyvcímekből álló listát kap paraméterül!
A függvény rendezze a könyvek címét Z-től A-ig (tehát először rendezze a listaelemeket ábécé sorrendbe,
majd fordítsa meg a rendezett listát)! A visszatérési érték az eredményül kapott lista.
Input: ['Vajak I', 'Allatfarm', 'Harry Potter es a bolcsek kove', 'A hobbit', 'Szamitogep Architekturak']
Return: ['Vajak I', 'Szamitogep Architekturak', 'Harry Potter es a bolcsek kove', 'Allatfarm', 'A hobbit']

'''

def könyveket_rendez(lista):
    for elotte in range(len(lista)):
        for mogotte in range(elotte+1,len(lista)):
            if lista[elotte]>lista[mogotte]:
                temp=lista[elotte]
                lista[elotte]=lista[mogotte]
                lista[mogotte]=temp
    lista.reverse()
    return lista

könyvek_lista=["Vajak ", "Allatfarm", "Harry Potter es a bolcsek kove", "A hobbit", "Szamitogep Architekturak"]

print (könyveket_rendez(könyvek_lista))