'''
Írjon egy scriptet, ami átmásol egy szövegfile-t, miközben ügyel arra, hogy minden sor nagybetűvel
kezdődjön
'''


with open("valami.txt","r",encoding="utf-8") as bemenet:
    with open("irott.txt","w",encoding="utf-8") as kimenet:
        for elem in bemenet:
            sor=elem.strip().capitalize()
            kimenet.write(sor+"\n")

























