'''
Írjon egy scriptet,ami lehetővé teszi egy olyan szövegfile kódolását,melynek minden sora különböző személyek vezetéknevét,
keresztnevét,címét,postai irányítószámát,és telefonszámát fogja tartalmazni.
(gondoljon például arra,hogy egy klub tagjairól van szó.)
'''
tagok = {"Vezeteknev": "Tóth",
         "Keresztnév": "János",
         "Cím": "Budapest Kázmér tér 6",
         "Irányítószám": 1000,
         "Telefonszám": 3630564897},\
        {"Vezeteknev":"Kiss",
         "Keresztnév":"Gergő",
         "Cím":"Kecskemét alsó út 4",
         "Irányítószám":3000,
         "Telefonszám":5620548976}
with open("valami.txt","w",encoding="utf-8") as file:
    for elem in tagok:
        elem["Születési idő"]= str(input("Kerem a születési időt: "))
        elem["Neme"] = str(input("Kerem a nemét: "))
    file.write(str(tagok))














































