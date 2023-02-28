#WAP to accept an 2D array from the user and to transpose it
r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
a=[]
for x in range (r):
    b=[]
    for y in range (c):
        b.append(int(input()))
    a.append(b)
for x in range(r):
    for y in range(c):
        print(a[x][y], end=" ")
    print()
print("Output:")
for x in range (c):
    for y in range (r):
        print(a[y][x],end=" ")
    print()