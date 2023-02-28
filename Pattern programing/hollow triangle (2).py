n1 = input ("Please enter the number")
n = int(n1)
j = 1
p = 1
l = 0
k = 0
i = 1
g = 1
d = 1
while (i <= (n-1)):
    k = k+4
    i = i+1
while (j <= n):
    if (g == n):
        while (d <= k):
            print ("*",end="")
            print ("",end="")
            d = d+1
    else:
        while (p <= l):
            print("  ", end="")
            p = p + 1
        l = l + 2
        print("*", end="")
        print()
        print("*", end="")
        p = 1
        j = j + 1
        g = g+1