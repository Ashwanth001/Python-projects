n1 = int (input ("Please enter the input in odd number"))
n = int(n1/2)
s = n
p = 1
cn1 = n1
s1 = 0
for q in range (n1):
    print ("*",end=" ")
print ()
for x in range (n):
    for y in range (s):
        print ("*",end=" ")
    for z in range (p):
        print (" ",end=" ")
    for t in range (s):
        print ("*",end=" ")
    s = s-1
    p = p+2
    print ()
for a in range (n1-n):
    for b in range (s1):
        print ("*",end=" ")
    for c in range (cn1):
        print (" ",end=" ")
    for e in range (s1):
        print ("*",end=" ")
    cn1 = cn1-2
    s1 = s1 + 1
    print ()
for q in range (n1):
    print ("*",end=" ")