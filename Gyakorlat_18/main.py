'''
Írjon egy programot,ami megvizsgálja egy számlista minden elemét,hogy két új listát hozzon létre. Az egyik csak az
eredeti lista páros számait tartalmazza a másik lista pedig csak a páratlanokat.
'''


t1 = [32,5,12,8,3,75,2,15]
t2=[]
t3= []
for elem in t1:
    if elem % 2 ==0:
        t2.append(elem)
    else:
        t3.append(elem)

print (t2)
print (t3)