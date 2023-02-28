n = int (input ("Please enter the length of the array"))
a = [0]*n
for x in range (0,n):
    print ("Location number",x+1)
    a[x] = int (input("Please enter an element"))
print ("The array you have entered is :")
for y in range (0,n):
    print (a[y],end ="")
    if (y < n-1):
        print (",",end="")
print ()
s = int(input("Please enter the search value"))
for z in range (0,n):
    if (a[z] == s):
        print ("The search value is present in the position",z+1)
        quit()
print ("The search value is not present")