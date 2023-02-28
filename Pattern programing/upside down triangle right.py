n1 = input ("Pleas enter the input")
n = int (n1)
i = 1
j = 1
s = n
while (i <= n):
    j = 1
    while (j <= s):
        print ("*",end="")
        j = j+1
    s = s-1
    i = i+1
    print ()