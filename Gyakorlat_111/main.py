'''
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját, és azt hogy rendelkezik-e
érvényes oltással veszettség ellen! Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!

'''

kutya_nev = input("Kerem a kutya nevét: ")
kutya_eletkor = input("Kerem a kutya korát: ")
kutya_fajta = input("Kerem a kutya fajtáját: ")
kutya_oltas = bool(input("Rendelkezik oltással? "))

kutya_adatok={"Nev":kutya_nev,"Kor":kutya_eletkor,"Fajta":kutya_fajta,"Oltás":kutya_oltas}
