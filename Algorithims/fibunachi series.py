n1 = input ("PLease enter the number: ")
n = int (n1)
n
a = 0
b = 1
c = 1
n = n - 3
s = 0
print (a," ",end="")
print (b," ",end="")
print (c," ",end="")
while (n > 0):
    s = a+b+c
    print (s," ",end="")
    a = b
    b = c
    c = s
    n = n-1
