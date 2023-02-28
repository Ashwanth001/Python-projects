r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
rows,columns = (r,c)
arr = [[0]*columns]*rows
print(arr)
for x in range (0,rows):
    for y in range (0,columns):
        arr[x][y] = int(input("Please enter a number"))
for x in range (0,rows):
    for y in range (0,columns):
        print(arr[x][y],"*",x,y,end=" ")
    print()
print(arr)