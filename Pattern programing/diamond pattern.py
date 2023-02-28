n = (int)(input("Please enter the input"))
l = n-1
p = 1
for x in range (n):
    for y in range (l):
        print (" ",end="")
    l = l-1
    for z in range (p):
        print ("*",end="")
    p = p+2
    print()
p = p-4
for a in range (n-1):
    for b in range (l+2):
        print (" ",end="")
    l = l+1
    for c in range (p):
        print ("*",end="")
    p = p-2
    print ()