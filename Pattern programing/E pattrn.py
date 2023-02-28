n = int (input ("Please enter the length in odd number"))
while (n % 2 == 0):
    n = int(input("Please enter the length in odd number"))
m = int ((n-1)/2)
c = 0
for x in range (n):
    if (c == 0 or c == m or c == n-1):
        for x in range (m+1):
            print ("*",end=" ")
        print()
        c = c+1
    else:
        print ("*")
        c = c + 1