'''
Írjon egy scriptet,ami úgy másol át egy file-t,hogy a szavak között megháromszorozza a szóközök számát.
Rendelkezésre áll egy szövegfile,aminek minen sora egy valós típusú numerikus érték reprezentációja (exponens nincs)
Például:
14.896
7894.6
123.278
stb
Írjon egy scriptet ami ezeket az értékeket egész számra kerekítve egy másik file-be másolja.
'''

with open("valami.txt","r",encoding="utf-8") as file:
    with open("valami2.txt","w",encoding="utf-8") as file_2:
        for elem in file:
            sor=elem.strip().replace(" ",3* " ")
            file_2.write(sor+"\n")


with open("szamok.txt","r",encoding="utf-8")as file:
    with open("szamok_2.txt","w",encoding="utf-8") as file_2:
        for elem in file:
            sor= elem.strip()
            sor=round(float(sor))
            sor= str(sor)
            file_2.write(sor+"\n")



































