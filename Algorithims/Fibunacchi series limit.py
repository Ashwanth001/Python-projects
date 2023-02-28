n1 = input ("Please enter the lower limit")
d1 = input ("PLease enter the upper limit")
d = int(d1)
n = int (n1)
i = 0
j = 1
a = 0
while (n <= d):
    while (j <=n):
        if (n % j == 0):
            i = i+1
        j = j+1
    if (i == 2):
        print (n," ",end="")
    n = n+1
    i = 0
    j = 1