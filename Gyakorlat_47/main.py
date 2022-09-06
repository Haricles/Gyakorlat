'''

Fejleszd tovább az első feladat programját,úgy hogy amennyiben a felhasználó nem két lehetséges válasz (igen/nem)
közül ad meg egyet,a gép kiírja: "sajnos nem értem a válaszodat!"
'''


a = input("Jó napja van? ")
if a == "igen" or a == "Igen" or a == "IGEN":
    print ("Nagyön örülök ennek.")
elif a == "nem" or a == "Nem" or a == "NEM":
    print("Ne búsúljon lesz még jobb is.")
else:
    print ("Sajnos nem értem a válaszodat! ")

