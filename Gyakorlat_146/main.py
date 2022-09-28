'''
Vágjon fö egy hosszú sztringet 5 karakter hosszú darabokra. Rakja össze a darabokat fordított sorrendben.
'''

karakter= "valamivanalevegőbenésnemtudomhogymi."

uj_karakter=""
i=0
for elem in karakter:
    if i % 5 ==0:
        uj_karakter+=(karakter[i:i+5])
    i+=1

print (uj_karakter[::-1])















































