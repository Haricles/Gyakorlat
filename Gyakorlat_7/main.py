# Írjon egy programot ami a következő jelsorozatot írja ki:
# *
# **
# ***
# ****
# *****
# ******
# *******


for i in range (1,8):
    print (i * "*")

# vagy while ciklussal:

i = 1
while i < 8:
    print (i * "*")
    i +=1