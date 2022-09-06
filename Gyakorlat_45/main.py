'''
Írjon egy programot,ami a felhasználótól bekéri az előszőr a keresztnevét majd a vezetéknevét. A program ezután
összefűzi ezeket egy teljes_nev nevű változóba. Végül a program a teljes nevén üdvözli a felhasználót.
'''

kereszt_nev= input("Kerem a keresztnevét: ")
vez_nev = input("Kerem a vezetéknevét: ")
teljes_nev= vez_nev+" "+kereszt_nev
print (f"Üdvözlöm,{teljes_nev}!")


