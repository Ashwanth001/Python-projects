n1 = input ("PLease enter the input: ")
n = int(n1)
k = 0
j = 1
i = 1
while (i <= n):
    k = k+i
    i = i+1
i = 1
while (i <= n):
    j = 1
    while (j <= i):
        print (k," ",end="")
        k = k-1
        j = j+1
    i = i+1
    print ()