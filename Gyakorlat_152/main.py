'''
Írjon   egy  nagybetu()  függvényt,aminek a visszatérési értéke akkor « igaz », ha az argumentuma nagybetű.
'''

def nagybetu(x):
    if x == x.capitalize():
        return True
    else:
        return False

print (nagybetu("Szia"))
print(nagybetu("szia"))



















