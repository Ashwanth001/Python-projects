n = int(input ("Please enter the length of the array"))
a = [0]*n
c = 1
for x in range (n):
    a[x] = int(input ("Please enter the value"))
for y in range (n-1):
    for z in range (n-1):
        c = c+1
        if (a[z] > a[z+1]):
            swap = a[z+1]
            a[z+1] = a[z]
            a[z] = swap
for b in range (n):
    print (a[b],end=" ")