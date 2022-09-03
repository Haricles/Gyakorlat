'''
Definiáljon egy indexMax(lista) függvényt,ami az argumentumként megadott lista legnagyobb értékű elemének az indexét
adja vissza.
'''


sorozat= [5,8,2,1,9,3,6,7]

def indexMax(lista):
    return lista.index(max(lista))

print (indexMax(sorozat))

def indexMax_2(*args):
    args = list(args)
    return args.index(max(args))

print (indexMax_2(2,7,9,1,2,6))