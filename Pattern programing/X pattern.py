n = (int) (input ("Please enter the input in odd number"))
j = 1
k = int ((n-1)/2)
h = 0
l = n-2
g = 1
q = int (((n-1)/2)-1)
while (n % 2 == 0):
    n = (int)(input("Please enter the input in (odd number)"))
for x in range (n):
    if (j == ((n+1)/2)):
        for y in range (k):
            print (" ",end="")
        j = j+1
        print ("*")
    else:
        j = j + 1
        if (j <= ((n+1)/2)):
            for z in range (h):
                print (" ",end="")
            h = h+1
            print ("*",end="")
            for a in range (l):
                print (" ",end="")
            l = l-2
            print ("*")
        else:
            for z in range (q):
                print (" ",end="")
            q = q-1
            print ("*",end="")
            for a in range (g):
                print (" ",end="")
            print ("*")
            g = g+2