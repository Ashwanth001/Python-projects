n = int (input ("Please enter the input"))
for x in range (1,n+1):
    for y in range (1,n+1):
        if (x == y ):
            print ("*",end="")
        elif ((x+y) == (n+1)):
            print ("*",end="")
        else:
            print(" ",end="")
    print ()