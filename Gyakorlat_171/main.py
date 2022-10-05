'''
Van egy file, amiben tanulók nevei találhatók. Írjon egy scriptet, ami rendezetten másolja át ezt a filet.

'''

with open("bemenet.txt", "r", encoding="utf-8") as file:
    with open("irott.txt","w",encoding="utf-8") as kimenet:
        for elem in file:
            sor=elem.strip()
            sor = sor.split(",")
            for elem in sor:
                kimenet.write(elem+"\n")


