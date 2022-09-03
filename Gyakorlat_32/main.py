'''
Definiáljon egy honapNeve(n) függvényt ami az év n-edik hónapjának a nevét adja vissza.
Pl: print (honapNeve(4)) eredménye : Április. 
'''


honapok = ["Január","Február","Március","Április","Május","Június",
           "Július","Augusztus","Szeptember","Október","November","December"]

def honapNeve(n):
    for elem in range(len(honapok)):
        return honapok[n-1]

print (honapNeve(4))