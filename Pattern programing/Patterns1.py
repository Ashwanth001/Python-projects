n = (int)(input ("Please enter the input"))
for x in range (n):
    for y in range (x):
        print (" ",end="")
    for z in range (x+1,n+1,1):
        print (z,end="")
    print()