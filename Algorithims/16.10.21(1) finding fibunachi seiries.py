n1 = input ("Please enter the input")
n = int(n1)
a = 1
b = 0
c = 0
test = 0
while (c <=n):
    c = a+b
    a = b
    b = c
    if (c == n):
        test = 1
if (test == 1):
    print ("It is a fibonacci number")
else:
    print ("It is not a fibonacci number")