'''
Írj egy szoveget_elemez nevű függvényt, amely egy szöveget vár paraméterben!
A függvény számolja meg, hogy a szövegben mennyi betű, számjegy és egyéb karakter szerepel,
majd adja ezt vissza egy dictionary-ben, a példában látható formátumban!
Input: 'Python4Life!!!'
Return: {'betu': 10, 'szamjegy': 1, 'egyeb': 3}

Input: '12345'
Return: {'betu': 0, 'szamjegy': 5, 'egyeb': 0}
'''
def szoveget_elemez(szoveg):
    szamlalok=[0]*3
    for elem in szoveg.lower():
        if (ord(elem)>97) and (ord(elem)<=122):
            szamlalok[0]+=1
        elif (ord(elem)>48) and (ord(elem)<=57):
            szamlalok[1]+=1
        else:
            szamlalok[2]+=1
    szotaram={}
    szotaram["betu"]=szamlalok[0]
    szotaram["szamjegy"]=szamlalok[1]
    szotaram["egyeb"]=szamlalok[2]
    return szotaram

sztring="Python4Life!!!"
print (szoveget_elemez(sztring))
sztring_2="12345"
print(szoveget_elemez(sztring_2))