'''
Informatikus szakon többféle kurzust is felvehetünk. Az informatikával kapcsolatos tárgyak kurzuskódja I betűvel,
a matekos tárgyak kurzuskódja M betűvel, míg a szabadon választható tárgyak kurzuskódja X betűvel kezdődik.

Írj egy kurzuskodot_csoportosit nevű függvényt, amely egy olyan szöveget kap paraméterül, ami pontosvesszővel
elválasztott kurzuskódokat tartalmaz! A függvény csoportosítsa a szövegben szereplő
kurzuskódokat "infós", "matekos" és "szabvál" kategóriákba, majd adja vissza az így kapott csoportosítást
egy dictionary-ben, a példában látható formátumban! Ha a paraméterben kapott érték az üres string,
akkor a függvény egy üres dictionary-vel térjen vissza!

Input: 'IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E'
Return: {'infos': ['IB370G', 'IB370E'], 'matekos': ['MBNXK114E', 'MBNXK114G'], 'szabval': ['XA0021-GTK-MM1']}

Input: 'ITN714G;IB402g;XN0011-01317;IB202g'
Return: {'infos': ['ITN714G', 'IB402g', 'IB202g'], 'matekos': [], 'szabval': ['XN0011-01317']}
Input: ''
Return: {}
'''
def kurzuskodot_csoportosit(szöveg):
    if szöveg=="":
        return {}
    kategoriak_szotar={}
    kategoriak_szotar["info"]=[]
    kategoriak_szotar["matekos"]=[]
    kategoriak_szotar["szabval"]=[]
    targyak_lista=szöveg.split(";")
    for elem in targyak_lista:
        if elem[0]=="i".upper():
            kategoriak_szotar["info"].append(elem)
        if elem[0]=="m".upper():
            kategoriak_szotar["matekos"].append(elem)
        if elem[0]=="x".upper():
            kategoriak_szotar["szabval"].append(elem)
    return kategoriak_szotar

sztring="IB370G;MBNXK114E;MBNXK114G;XA0021-GTK-MM1;IB370E"
print (kurzuskodot_csoportosit(sztring))
sztring_2="ITN714G;IB402g;XN0011-01317;IB202g"
print(kurzuskodot_csoportosit(sztring_2))
sztring_3=""
print(kurzuskodot_csoportosit(sztring_3))