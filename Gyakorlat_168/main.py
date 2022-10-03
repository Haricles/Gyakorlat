'''
Írjon egy scriptet, ami úgy másol át egy szövegfilet, hogy azokat a sorokat, amik kisbetűvel kezdődnek
összeolvasztja az előző sorral.
'''

with open("valami.txt","r",encoding="utf-8") as bemenet:
    with open("irott.txt","w",encoding="utf-8") as kimenet:
        for elem in bemenet:
            sor_0=elem.strip()
            if elem[0] != elem[0].upper():
                sor_1 = elem.strip()
                kimenet.write(sor_1)
            else:
                kimenet.write("\n"+sor_0)






























