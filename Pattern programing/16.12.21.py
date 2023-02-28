n = int (input("Please enter the length array"))
a = [0]*n
b = [0]*n
for x in range (0,n):
    print ("Location number for spaces",x+1)
    a[x] = int (input())
    print("Location number for dots",x+1)
    b[x] = int(input())
for y in range (n):
    for z in range (a[y]):
        print (" ",end="")
    for z in range (b[y]):
        print ("*",end="")
    print ()
