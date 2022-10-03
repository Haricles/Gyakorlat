'''
Írjon egy egy ASCII kódtáblát kiíró scriptet. A programnak minden karaktert ki kell írni. A táblázat
alapján   állapítsa   meg   a   nagybetűs   és   kisbetűs   karaktereket   összekapcsoló   relációt   minden   egyes
karakterre.

'''
i=0
while chr(i) < chr(128):
    if i >= 65 and i <= 90:
        print ("Ez a nagybetű",chr(i))
    elif i >= 97 and i <=122:
        print ("Ez kisbetű",chr(i))
    else:
        print (chr(i))
    i+=1


