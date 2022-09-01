'''
Írjon egy programhurkot,ami a felhasználótól kéri a tanulok érdemjegyeit. A hurok csak akkor fejeződjön be ha a felhasz-
náló negatív értéket ír be.A beirt jegyekkel hozzon létre egy listát. Minden jegy beiírása után irassa ki a listát és
a beírt jegyek számát és legnagyobb / legkisebb értéket és az átlagot.
'''


t1 = []
a = 0
while a >= 0:
    a = int(input("Kerem az osztályzatod: "))
    if a >= 0:
        t1.append(a)
    print ("Az osztályzatok: ",t1)
    b = len(t1)
    print ("Lista elemeinek száma: ",b)
    print ("Maximum érték: ",max(t1))
    print("Minimum érték: ",min(t1))
    print ("Átlag",sum(t1) / b)





