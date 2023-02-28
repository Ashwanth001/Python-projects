#WAP to create a 2d list with r rows and c columns
#Fill the entire matrix such that the element present in the cell is the product of its row, column address
r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
sum = 0
for x in range (r):
    for y in range (c):
        sum = x*y
        print(sum,end=" ")
        
    print()

