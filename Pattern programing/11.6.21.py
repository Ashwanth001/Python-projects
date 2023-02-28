w = 0
while (w % 2 == 0):
    w = (int (input("Please enter the width in odd number")))
l = (int (input("Please enter the length")))
for x in range (1,l+1):
    if (x == 1 or x == l):
        for y in range (w*2+5):
            print ("*",end="")
        print ()
    else:
        for z in range (w+1*2):
            print ("* ",end="")
        print ("*")