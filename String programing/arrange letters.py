n = int (input ("Input the length of the array"))
a = [""]*n
b = [0]*n
for x in range (0,n):
    a[x] = input ("Please enter the alphabet")
print ("The characters you have typed are")
for y in range (n):
    print (a[y],end=" ")
print ()
for z in range (n):
    b[z] = ord(a[z])
print ()
for c in range (0,n-1):
    min = b[c]
    pos = c
    for d in range (c+1,n):
        if (b[d] < min):
            min = b[d]
            pos = d
    swap = b[c]
    b[c] = min
    b[pos] = swap
for y in range(n):
    print(chr(b[y]),end=" ")
print()