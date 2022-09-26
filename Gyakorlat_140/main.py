'''
Írj egy Python eljárást, amely paraméterként kap egy pozitív egész számot és kiír a képernyőre
ennyi karaktert úgy, hogy minden harmadik karakter pluszjel (+) legyen a többi viszont
mínuszjel (-)! A programodban hívd is meg ezt az alprogramot!
'''

def pluszjel(a):
    for elem in range(a):
        if elem % 3 ==0:
            print ("+",end="")
        else:
            print ("-",end="")




pluszjel(3)






















