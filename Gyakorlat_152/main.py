'''
Írjon   egy  nagybetu()  függvényt,   aminek   a   visszatérési   értéke   akkor   « igaz »,   ha   az   argumentuma
nagybetű.
'''

mondat="van Benne nagy betű"
def nagybetü(x):
    abc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    index=0
    for elem in mondat:
        if elem in abc:
            break
        else:
            index+=1
    if index < len(mondat):
        return True
    else:
        return False


print (nagybetü(mondat))


