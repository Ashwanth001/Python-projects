n1 = input ("Please enter the input")
n =int(n1)
b = 1
c = 0
w = 1
j = 1
k = 0
s = 1
r = 1
i = 0
while (r <= n-1):
    w = w+2
    r=r+1
g = w-4
while (s <= w):
    print ("*",end="")
    s = s+1
print ()
while (b<=n-2):
    while (c <= k):
        print (" ",end="")
        c =c+1
    print ("*",end="")
    c = 0
    k = k+1
    while (j <= g):
        print (" ",end="")
        j = j+1
    j = 1
    g = g-2
    b=b+1
    print ("*")
while (i <= n-2):
    print (" ",end="")
    i = i+1
print ("*")