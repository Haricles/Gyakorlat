'''
Írjon egy programot ami egy szavakból álló lista elemeit egyenként megvizsgálja azért,hogy két új listát hozzon létre.
Az egyikben 6 karakternél rövidebb szavakat a másikban 6 , vagy annál több karaktert tartalmazó szavak legyenek.
'''

t1= ["Jean","Maximilien","Brigitte","Sonia","Jean-Pierre","Sandra"]
t2=[]
t3 = []
for elem in t1:
    if len(elem) < 6:
        t2.append(elem)
    else:
        t3.append(elem)

print (t2)
print (t3)


