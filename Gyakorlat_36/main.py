'''
Írjon egy scriptet ami lehetővé teszi egy szövegfile kényelmes olvasását. A program előszőr kérje a felhasználótól
a file nevét. Ezután ajánlja föl a következő választást: új szövegsorokat rögzít vagy ki írja a file tartalmát.
A felhasználónak be kell tudnia írni az egymást követő szövegsorokat, az <entert> használva a szövegsorok elválasztására
A beírás befejezéseként elég egy üres sor bevinni (vagyis elég magában leütni az entert). A tartalom kiírásakor
a soroknak természetes módon kell egymást után következni.
'''
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
