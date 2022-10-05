'''
Legyenek adottak a következő listák :
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Január','Február','Március','Április','Május','Június',
 'Július','Augusztus','Szeptember','Október','November','December']
Írjunk  egy  kis  programot,  ami  a  második  listába  úgy  szúrja   be   az   első  lista   összes  elemét, hogy
minegyik   hónap   nevét   az   illető   hónap   napjainak   száma   követi : ['Január',31,'Február',
28,'Március',31, stb...].

'''
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Január','Február','Március','Április','Május','Június',
 'Július','Augusztus','Szeptember','Október','November','December']
t3=[]


for elem in range(len(t1)-1):
    t3.append(t2[elem])
    t3.append(t1[elem])

print (t3)
