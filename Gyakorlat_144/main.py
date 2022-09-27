'''
Az A és B már létező file-okból konstruáljon egy harmadik C file-t,ami felváltva tartalmaz egy-egy elemet az A illetve
B file-ból. Amikor elérte az egyik eredeti file végét,akkor egészítse ki a C file-t a másik file maradék elemeivel.
'''

file_1_tomb=[]
file_2_tomb=[]
valtott_sorok=[]

with open("valami.txt","r",encoding="utf-8") as file_1:
    with open("valami2.txt", "r", encoding="utf-8") as file_2:
        for elem in file_1:
            sor_1=elem.strip()
            file_1_tomb.append(sor_1)
        for sor in file_2:
            sor_2=sor.strip()
            file_2_tomb.append(sor_2)


if len(file_1_tomb) < len(file_2_tomb):
    max_index=len(file_1_tomb)
else:
    max_index=len(file_2_tomb)
index =0
while index < max_index:
    a=file_1_tomb[index]
    b=file_2_tomb[index]
    valtott_sorok.append(a)
    valtott_sorok.append(b)
    index+=1

if len(file_1_tomb) == max_index:
    for i in range(max_index,len(file_2_tomb)):
        valtott_sorok.append(file_2_tomb[i])
else:
    for i in range(max_index,len(file_1_tomb)):
        valtott_sorok.append(file_1_tomb[i])

with open("versek.txt","w",encoding="utf-8") as versek:
    for elem in valtott_sorok:
        versek.write(elem+"\n")








































