n = (int)(input("Please enter the input"))
p = 1
c = 2
f = 0
for x in range (n):
    p = x+1
    for y in range (n):
        while (p > 0):
            for z in range (2,c):
                if (c % z == 0):
                    f = f+1
            if (f==0):
                print (c,end=" ")
                p = p-1
            f = 0
            c = c+1
    print ()