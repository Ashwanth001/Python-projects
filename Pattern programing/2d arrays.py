c = 5
r = 5
a = [[0]*c]*r
for x in range (0,5):
    a[0][x] = input("Please enter the name")
for x in range (0,5):
    a[1][x] = input("Please enter the class")
for x in range (0,5):
    a[2][x] = input("Please enter the age")
for x in range (0,5):
    a[3][x] = input("Please enter the city")
for x in range (0,5):
    a[4][x] = input("Please enter the number")
n = input("Please enter the name")
for x in range (0,5):
    if (a[0][x] == n):
        for y in range (1,5):
            print(a[y][x])