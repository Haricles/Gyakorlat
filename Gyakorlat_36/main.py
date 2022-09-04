
with open (input("Kerem a file nevét: "),input("Új szövegsorokat rögzít vagy ki írja a file tartalmát?(a vagy r): "),
           encoding="utf-8") as file:

    ujsor= input("Kerem a szöveget: ")
    while ujsor != "":
        file.write("\n"+ujsor)
        ujsor = input("Kerem a szöveget: ")

#ellenőrzés miatt nyitottam meg olvasásba.
with open("Atlas-enUS.lua","r",encoding="utf-8") as olvaso:
    for sor in olvaso:
        print (sor.strip())
