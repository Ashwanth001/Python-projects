n = input ("Please enter the input")
l = len (n)
cn = n
c = 1
for x in range (l+1):
    if (c % 2 == 0):
        for y in range (x):
            print (cn[y],end="")
        print ()
        c = c+1
    else:
        cl = l-1
        for z in range (x):
            print (cn[cl],end="")
            cl = cl-1
        cl = l-1
        print ()
        c = c+1