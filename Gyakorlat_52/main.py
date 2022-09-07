'''

Készíts egy programot,amely a felhasználtó által megadott egész számról eldönti,hogy csak
-3-al osztható
-csak 4-el osztható
-3-mal és 4-gyel is osztható
-sem 3-al sem 4-gyel nem osztható
'''

bemenet= int(input("Kérem a számot: "))
if bemenet % 3 ==0 and bemenet % 4 != 0:
    print ("3-al osztható!")
elif bemenet % 4 == 0 and bemenet % 3 !=0:
    print ("4-gyel osztható!")
elif bemenet % 3 == 0 and bemenet % 4 == 0:
    print ("3-al és 4-gyel is osztható!")
else:
    print ("Sem 3-al sem 4-gyel nem osztható! ")