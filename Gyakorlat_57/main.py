'''
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja.
 Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen kívül és ne tárolja.
 A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)!
 A program a bekért neveket írja ki a képernyőre!
A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!
'''

tarolo = []
bemenet = None
while bemenet !="":
    bemenet = input("Kerem az 'a' betüvel keződő szavakat,ha nem 'a' betüvel keződik nem tudom tárolni: ").lower()
    if bemenet != "" and bemenet[0] == "a":
        tarolo.append(bemenet)
print(f"Az ön szavai:{tarolo}")










