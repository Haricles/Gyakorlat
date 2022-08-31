# Írjon egy programot,ami megkeresi egy lista legnagyobb és legkisebb elemét.

t1 = [32,5,12,8,3,75,2,15]
legkisebb = t1[0]

for elem in t1:
    if legkisebb > elem:
        legkisebb = elem
print ("A legkisebb szam a listaban:",legkisebb)

for elem in t1:
    if legkisebb < elem:
        legkisebb = elem
print ("A legnagyobb szam a listaban:",legkisebb)

'''
a másik módszer:
'''

print ("A legkisebb szam a listaban_2: ",min(t1))
print ("A legnagyobb szam a listaban_2: ",max(t1))