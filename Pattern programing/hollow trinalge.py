v = int (input ("Please enter input"))
k= 1
for x in range (v-1):
    for y in range (v-k):
        print (" ",end="")
    for z in range (1,(2*k)):
        if (z == 1 or z == ((2*k)-1)):
            print ("*",end="")
        else:
            print(" ", end="")
    k = k+1
    print()
for z in range (1,(2*k)):
    print ("*",end="")