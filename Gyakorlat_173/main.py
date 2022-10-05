'''
. Írjon egy scriptet, ami kiíratja egy csütörtöki nappal kezdődő képzeletbeli év napjainak a listáját. A
scriptben három lista lesz : az egyik a hét napjainak a neveit fogja tartalmazni, a másik a hónapok
neveit, a harmadik pedig hogy hány naposak a hónapok (a szökőéveket nem vesszük figyelembe).
Példa  :
Január 1 csütörtök  Január 2 péntek  Január 3 szombat  Január 4 vasárnap
és így tovább  December 31 csütörtök-ig.
'''

honapok=["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
het_napjai=["Csütörtök","Péntek","Szombat","Vasárnap","Hétfő","Kedd","Szerda"]
napok=[31,28,31,31,30,30,31,30,31,30,31,30]
eredmeny=[]
j=0
temp=[]
for i,honap in enumerate(honapok):
    for nap in range(1,napok[i]+1):
        if j % 7 ==0:
            j = 0
        temp.append(honap)
        temp.append(nap)
        temp.append(het_napjai[j])
        eredmeny.append(temp)
        temp=[]
        j+=1
print (eredmeny)







