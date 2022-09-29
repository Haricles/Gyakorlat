'''
Írjon   egy  nagybetu()  függvényt,   aminek   a   visszatérési   értéke   akkor   « igaz »,   ha   az   argumentuma
nagybetű.
'''

mondat="van Benne nagy betű"
def nagybetü(x):
    index=0
    while index < len(x):
        if x[index]== x[index].capitalize():
            break
        else:
            index+=1
    if index < len(x):
        return True
    else:
        return False

print (nagybetü(mondat))



