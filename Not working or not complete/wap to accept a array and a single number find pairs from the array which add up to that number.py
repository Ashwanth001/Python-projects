n = int(input("Please enter the length of the array"))
a = [0]*n
s = int(input("Please enter the search value"))
for x in range (n):
    a[x] = int(input("Please enter the value"))
for y in range (n-1):
    for z in range (n):
