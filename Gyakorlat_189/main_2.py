'''
Ricsi nagyon szereti a sorozatokat... mármint a matematikai sorozatokat. Kedvencei a számtani és mértani sorozatok.
Írj egy sorozat nevű függvényt, amely egy számokból álló listát kap paraméterül!
A függvény döntse el, hogy a listában szereplő számok számtani, illetve mértani sorozatot alkotnak-e!

Kezeld le azt az esetet, amikor a függvény paraméterében érkező lista 3-nál kevesebb elemet tartalmaz!
Ekkor a visszatérési érték a HIBA! szöveg legyen! Egyéb hibakezeléssel nem kell foglalkoznod.
Input: [10, 20]
Return: 'HIBA!'

Input: [2, 3, 5, 7, 11, 13]
Return: 'A sorozat se nem szamtani, se nem mertani sorozat.'

Input: [42, 42, 42]
Return: 'A sorozat szamtani es mertani sorozat is egyben.'

Input: [9, 5, 1, -3, -7]
Return: 'A sorozat szamtani sorozat.'

Input: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
Return: 'A sorozat mertani sorozat.'
'''
def sorozat(lista):
    if len(lista) < 3:
        return "HIBA!"

    szamtani = True
    mertani=True
    szamtani_soroazat=lista[1] - lista[0]
    mertani_sorozat=lista[1] / lista[0]

    for elem in range(1,len(lista)-1):
        if lista[elem+1]-lista[elem] != szamtani_soroazat:
            szamtani=False
        if lista[elem+1] / lista[elem] != mertani_sorozat:
            mertani = False

    if szamtani and mertani:
        return "A sorozat szamtani és mértani is."
    elif szamtani:
        return "A sorozat szamtani."
    elif mertani:
        return "A sorozat mertani."
    else:
        return "A sorozat se nem szamtani sem pedig mertani"

lista=[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(sorozat(lista))