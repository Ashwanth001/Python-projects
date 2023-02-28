def symbol_star (q):
    s = 1
    for x in range (1,n+1):
        for y in range (n-x):
            print (" ",end="")
        for z in range (s):
            print ("*",end="")
        s = s+2
        print ()
def symbol_at (w):
    p = 1
    for a in range (1,n+1):
        for b in range (n-a):
            print (" ",end="")
        for c in range (p):
            print ("@",end="")
        p = p+2
        print ()
n = int(input("Please enter the length"))
c = int(input("Please enter 1 for star and 2 for @"))
if (c == 1):
    symbol_star(n)
else:
    symbol_at(n)