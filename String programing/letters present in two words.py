n1 = input("Please enter the first word")
b = input ("Please enter second word")
l = len(n1)
c = ""
d = ""
u = n1[0]
l2= len(u)
dup = 0
bl = len(b)
bc = ""
for x in range (0,l):
    c = n1[x]
    for y in range (0,l2):
        if (c == u[y]):
            dup = dup+1
    if (dup == 0):
        u = u+c
    dup = 0
    l2 = len(u)
temp = 0
for c in range (0,l2):
    uc = u[c]
    for d in range (0,bl):
        bc = b[d]
        if (uc == bc):
            temp = temp+1
    if (temp > 0):
        print (uc,"is present")
    else:
        print (uc,"is absent")
    temp = 0