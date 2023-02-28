n1 = input ("Please enter the input")
n= int(n1)
s= 1
p = 0
v = 1
while (v <= n):
    if (v == 1 or v == n):
        while (s <= n):
            print("*",end="")
            s= s+1
    else:
        while (s<=p):
            print (" ",end="")
            s= s+1
        p = p+1
        print ("*",end="")
    s = 1
    v = v+1
    print ()