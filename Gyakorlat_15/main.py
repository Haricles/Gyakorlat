# Írjon egy programot,ami egy új t3 listát hoz létre. Ennek felváltva kell tartalmazni a két lista mindel elemét
# úgy,hogy , minden hónap nevét követnie kell a megfelelő napok számának: ["Január",31,"Február",28]

t1= ["Január","Február","Március","Áprlis","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
t2 = [31,28,31,30,31,30,31,31,30,31,30,31]
t3 = []

index = 0
while index < len(t1):
    a = t1[index]
    b = t2[index]
    t3.append(a)
    t3.append(b)
    index+=1
print (t3)

