n = (int) (input ("Please enter the input"))
j=0
o = 1
p = n+1
q = n
for x in range (n):
    for y in range (p):
        print ("*",end="")
    p = p-1
    for z in range (o):
        print (o,end="*")
    o = o+1
    for w in range (q):
        print ("*",end="")
    q = q-1
    print()