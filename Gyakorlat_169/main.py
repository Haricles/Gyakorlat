'''
Van  egy  numerikus   értékeket  tartalmazó   file.  Tegyük  fel,  hogy  ezek  az   értékek  egy  gömbsorozat
átmérői.  Írjon   egy   scriptet,   ami   arra   használja   föl   ennek   a   file­nak   az   adatait,hogy egy másik
szövegsorokba rendezett filet hoz létre, ami ezeknek a gömböknek más jellemzőit fejezi ki (főkör
területe, felület, térfogat) a következő formában :

d 46.20 cm Ft = 1676.39 cm² Fel. = 6705.54 cm². Tf. = 51632.67 cm³
d. 120.00 cm Ft = 11309.73 cm² Fel. = 45238.93 cm². Tf. = 904778.68 cm³
d. 0.03 cm Ft = 0.00 cm² Fel. = 0.00 cm². Tf. = 0.00 cm³
d. 13.90 cm Ft = 151.75 cm² Fel. = 606.99 cm². Tf. = 1406.19 cm³
d. 88.80 cm FT = 6193.21 cm² Fel. = 24772.84 cm². Tf. = 366638.04 cm³

'''
import math

def fökör_terület(x):
    r =x / 2
    return (r**2) * math.pi

def gömb_felszin(x):
    r = x /2
    return 4*r**2*math.pi

def gömb_terfogat(x):
    r = x / 2
    return (4*(r**3)*math.pi) / 3

with open("valami.txt","r",encoding="utf-8") as bemenet:
    with open("irott.txt","w",encoding="utf-8") as kimenet:
        for elem in bemenet:
            a= float(elem.strip())
            x= f"{a} cm Ft = {round(fökör_terület(a),2)} cm² Fel. = {round(gömb_felszin(a),2)} cm². Tf. = {round(gömb_terfogat(a),2)} cm3"
            kimenet.write(str(x)+"\n")






























