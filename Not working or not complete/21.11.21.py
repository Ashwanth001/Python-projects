n = int (input ("Please enter the length of the array"))
a = [0]*n
for x in range (0,n):
    print ("The location number",x+1)
    a[x] = int (input ("Please enter the value"))
for y in range (0,n-1):
    max = a[y]
    pos = a[y]
    for z in range (y+1,n):
        if (a[z] > max):
            max = a[z]
            pos = z
    swap = a[y]
    a[y] = max
    a[pos] = swap
    for b in range (n):
        print (a[b],end=" ")
    print ()