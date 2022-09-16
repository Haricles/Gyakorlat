'''
Írj egy programot, amely a fenti listából kiszűri az 'l' betűt tartalmazó szavakat kétféleképpen:
filter() + lambda függvény és list comprehension segítségével is!


'''


szavak = ['alma', 'ló', 'padló', 'citrom', 'kávé', 'nyugalom']

eredmeny= [print("List compresension:",elem) for elem in szavak if "l" in elem]

print (list(filter(lambda szo: "l" in szo,szavak)))



