n = (int) (input("Please enter the input"))
j = 1
o = n*2
g = n
f = 1
k = n
q = 0
u = 1
t = o-1
e = 1
for x in range (o+2):
    if (j == 1 or j == o+2):
        for y in range (o+1):
            print ("*",end="")
        print ()
        j = j+1
    else:
        if (q < n*2/2):
            for z in range (g):
                print ("*",end="")
            g = g-1
            for a in range (f):
                print(" ",end="")
            f = f+2
            for b in range (k):
                print("*",end="")
            print()
            k = k-1
            q = q+1
            j = j+1
        else:
            for z in range (u):
                print ("*",end="")
            u = u+1
            for a in range (t):
                print(" ",end="")
            t = t-2
            for b in range (e):
                print("*",end="")
            print()
            q = q+1
            e = e+1
            j = j+1