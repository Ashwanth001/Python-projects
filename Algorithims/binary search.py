n = int(input("Please enter the length of the array"))
a = [0]*n
swap = 0
for x in range (n):
    a[x] = int(input("Please enter the value"))
for y in range (0,n):
    pos = y
    min = a[y]
    for z in range (y+1,n):
        if (a[z] < min):
            pos = z
            min = a[z]
    swap = a[y]
    a[y] = min
    a[pos] = swap
for b in range (n):
    print (a[b],end=" ")
print ()
s = int (input ("Please enter the search element"))
ub = n-1
lb = 0
m = int((ub+lb)/2)
while (lb < ub):
    if (a[m] == s):
        print ("Element found at position",m+1)
        quit()
    elif (a[m] < s):
        lb = m+1
        m = int((lb+ub)/2)
    else:
        ub = m-1
        m = int((lb+ub)/2)
print ("The element was not present")