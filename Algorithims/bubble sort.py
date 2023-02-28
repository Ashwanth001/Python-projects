# selection sort
n = int (input ("Please enter the length of the array"))
a = [0]*n
for x in range (0,n):
    print ("The location number",x+1)
    a[x] = int (input ("Please enter the value"))
for z in range (0,n-1):
    min = a[z]
    pos = z
    for y in range(z+1,n):
        if (a[y] < min):
            min = a[y]
            pos = y
    swap = a[z]
    a[z] = a[pos]
    a[pos] = swap
    print ("After pass:",z)
    for b in range (n):
        print (a[b],end=" ")