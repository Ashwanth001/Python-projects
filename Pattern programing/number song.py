n1 = input ("Please enter the input")
n = len (n1)
s = n-1
i = 0
s1 = 0
for x in range (n):
    for y in range (s):
        print (" ",end="")
    s = s-1
    print (n1[i],end="")
    for z in range (s1):
        print(" ",end="")
    if (s1 == 0):
        print ()
        s1 = 1
    else:
        print (n1[i])
        s1 = s1+2
    i = i+1