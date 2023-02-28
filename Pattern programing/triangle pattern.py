n1 = input ("Please enter the input")
n = int(n1)
i = 1
j = 1
a = 1
while (i <= n):
    while (j <= i):
        print (a," ",end="")
        j = j+1
    i = i+1
    a = a+1
    j = 1
    print ()