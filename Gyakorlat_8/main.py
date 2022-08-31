# Írjon egy programot amit a bankban elhelyezett 4.3 %-os kamatozású tőke 20év alatt felhhalmozódott évi kamatait
# számolja ki.

toke = 10000
for i in range(1,20):
    print (i*toke*0.043+toke)