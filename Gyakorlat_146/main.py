'''
Vágjon fö egy hosszú sztringet 5 karakter hosszú darabokra. Rakja össze a darabokat fordított sorrendben.
'''

karakter= "valamivanalevegőbenésnemtudomhogymi."
#1.megoldás:
uj_karakter=""
i=0
for elem in karakter:
    if i % 5 ==0:
        uj_karakter+=(karakter[i:i+5])
    i+=1

print (uj_karakter[::-1])


#2.megoldás:
i=1
temp=""
tömb=[]
for elem in karakter:
    if i % 5==0:
        temp+=elem
        tömb.append(temp)
        temp=""
    else:
        temp+=elem
    i+=1
tömb.append(temp)

uj_valtozo=""
for elem in reversed(tömb):
    uj_valtozo+=elem
print (uj_valtozo)




