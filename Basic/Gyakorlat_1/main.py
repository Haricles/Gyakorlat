szöveg = input("Kerem a szöveget: ").upper()
kulcs = input("Kerem a kulcsot: ").upper()
betük= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","X","Y","Z"]

eredmeny=""
for j,k in enumerate(szöveg):
    print (szöveg[j],"",kulcs[j])
    a= betük.index(szöveg[j])+ betük.index(kulcs[j])
    a = a % len(betük)
    eredmeny=eredmeny + betük[a]
print (eredmeny)








