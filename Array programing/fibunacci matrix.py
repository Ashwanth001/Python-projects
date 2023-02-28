#WAP to create a 2D array and fill it with fibonacci numbers
r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
sum = 0
print("0",end=" ")
print("1",end=" ")
print("1")
a=1
b=2
for x in range (r):
    for y in range (c):
        sum = a+b
        a=b
        b=sum
        print(sum,end=" ")
    print()
#WAP to create a 2D array fill it with elements accepted from the user and then develop find and replace funtionality to take user input and make changes inside the existing 2D array.
