n = input("Please enter the input")
i= 1
j = 0
l = len(n)
c = 1
for x in range (l):
    for y in range (i):
        for z in range (c):
            print (n[j],end="")
        j = j+1
    j = 0
    c = c+1
    i = i+1
    print ()
