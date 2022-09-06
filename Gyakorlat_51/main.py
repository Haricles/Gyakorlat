'''

Készíts egy programot,amely a felhasználtól két külön kérdésben megkérdezi,hogy az ikerek(Henrik és Hanna)
jönnek-e kosarazni! A program írja ki,hogy melyik állítás igaz az alábbiak közül
-egyikük sem jön kosarazni
-mind a ketten jönnek kosarazni
-csak az egyikük jön kosarazni

'''

henrik= input("Henrik,jössz ma kosarazni? ")
hanna = input("Hanna,jössz ma kosarazni? ")
if henrik == "igen" and hanna == "igen":
    print ("Mind a ketten jönnek kosarazni! ")
elif (henrik=="igen" and hanna == "nem") or (henrik=="nem" and hanna == "igen"):
    print ("Csak az egyikük jön! ")
else:
    print ("Egyikük sem jön kosarazni! ")



