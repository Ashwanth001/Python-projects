#WAP to create a 2D array fill it with elements accepted from the user and then develop find and replace funtionality to take user input and make changes inside the existing 2D array.
r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
a=[]
for x in range (r):
    b=[]
    for y in range (c):
        b.append(int(input()))
    a.append(b)
for x in range (r):
    for y in range (c):
        print(a[x][y],end=" ")
    print()
s = int(input("Please enter the element to be replaced"))
n = int(input("Please enter the value that is to be replaced with the desired element"))
for x in range (r):
    for y in range (c):
        if a[x][y] == s:
            a[x][y] = n
for x in range (r):
    for y in range (c):
        print(a[x][y],end=" ")
    print()


