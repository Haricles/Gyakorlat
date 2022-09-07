'''
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő szavakat is elfogadja.
'''
# Az előző feladatot is úgy oldottam meg,hogy figyeltem arra,hogy a "A" betűt is elfogadja. 
tarolo = []
bemenet = None
while bemenet !="":
    bemenet = input("Kerem az 'a' betüvel keződő szavakat,ha nem 'a' betüvel keződik nem tudom tárolni: ").lower()
    if bemenet != "" and bemenet[0] == "a":
        tarolo.append(bemenet)
print(f"Az ön szavai:{tarolo}")










